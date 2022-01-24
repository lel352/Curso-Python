from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Post

class PostIndex(ListView):
    model = Post  # sobre escrevendo coisas do ListView
    template_name = 'posts/index.html'
    paginate_by = 1
    context_object_name = 'posts' # interavel para for


class PostBusca(PostIndex):
    pass


class PostCategoria(PostIndex):
    pass


class PostDetalhes(UpdateView):
    pass


