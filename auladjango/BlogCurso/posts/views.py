from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Post
from django.db.models import Q, Count, Case, When
from comentarios.forms import FormComentario
from comentarios.models import Comentario
from django.contrib import messages
from django.db import connection

class PostIndex(ListView):
    model = Post  # sobre escrevendo coisas do ListView
    template_name = 'posts/index.html'
    paginate_by = 1
    context_object_name = 'posts' # interavel para for

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.select_related('categoria_post')
        qs = qs.order_by('-id').filter(publicado_post=True) # id de forma decresente e o campo tem que estar publicado para aparecer
        qs = qs.annotate( # Criando um campo chamado numero_comentarios
            numero_comentarios=Count(
                Case(
                    When(comentario__publicado_comentario=True, then=1)  # Na tabela comentario pegando o campo publicado_comentario, dizendo para contar 1
                )
            )
        )

        return qs

    """def get_context_data(self, *, object_list=None, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['connection'] = connection
        return contexto Quantas consultas realizadas
        """


class PostBusca(PostIndex):
    template_name = 'posts/post_busca.html'

    def get_queryset(self):
        qs = super().get_queryset()
        termo = self.request.GET.get('termo')

        if not termo:
            return qs

        qs = qs.filter(
            Q(titulo_post__icontains=termo) | #icontains não casesensitive
            Q(autor_post__first_name__iexact=termo) |
            Q(conteudo_post__icontains=termo) |
            Q(excerto_post__icontains=termo) |
            Q(categoria_post__nome_cat__iexact=termo)
        )

        return qs



class PostCategoria(PostIndex):
    template_name = 'posts/post_categoria.html'

    def get_queryset(self):
        qs = super().get_queryset() # reutiliza o codigo usado no index acima
        categoria = self.kwargs.get('categoria', None)
        if not categoria:
            return qs

        qs = qs.filter(categoria_post__nome_cat__iexact=categoria)  # campo do Post(FK) dentro de Categoria o campo

        return qs

# Como estava antes
# class PostDetalhes(UpdateView):
#     template_name = 'posts/post_detalhes.html'
#     model = Post
#     form_class = FormComentario
#     context_object_name = 'post'
#
#     def get_context_data(self, **kwargs):
#         contexto = super().get_context_data(**kwargs)
#         post = self.get_object()
#         comentarios = Comentario.objects.filter(publicado_comentario=True, post_comentario=post.id)
#         contexto['comentarios'] = comentarios
#         return contexto
#
#     def form_valid(self, form):
#         post = self.get_object()
#         comentario = Comentario(**form.cleaned_data)
#         comentario.post_comentario = post
#
#         if self.request.user.is_authenticated:
#             comentario.usuario_comentario = self.request.user
#
#         comentario.save()
#         messages.success(self.request, 'Cometários enviado com sucesso.')
#
#         return redirect('post_detalhes', pk=post.id)


class PostDetalhes(View):
    template_name = 'posts/post_detalhes.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        pk = self.kwargs.get('pk')
        post = get_object_or_404(Post, pk=pk, publicado_post=True)
        comentarios = Comentario.objects.filter(publicado_comentario=True, post_comentario=post.id)
        self.contexto = {'post': post,
                    'comentarios': comentarios,
                    'form': FormComentario(request.POST or None),
         }


    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.contexto)

    def post(self, request, *args, **kwargs):
        form = self.contexto['form']
        if not form.is_valid():
            return render(request, self.template_name, self.contexto)

        comentario = form.save(commit=False)
        if request.user.is_authenticated:
           comentario.usuario_comentario = request.user

        comentario.post_comentario = self.contexto['post']
        comentario.save()
        messages.success(self.request, 'Cometários enviado com sucesso.')
        return redirect('post_detalhes', pk=self.kwargs.get('pk'))

