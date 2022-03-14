from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.contrib import messages
from django.http import HttpResponse
from . import models
from pprint import pprint
import produto
# Create your views here.


class ListaProdutos(ListView):
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = 3
    # USANDO PARA TESTE
    #def get(self, *args, **kwargs):
    #    return HttpResponse('pAGAR')

class DetalheProdutos(DetailView):
    model = models.Produto
    template_name = 'produto/detalhe.html'
    context_object_name = 'produto'
    slug_url_kwarg = 'slug'

class AdicionarAoCarrinho(View):
    def get(self, *args, **kwargs):
        # TODO:Remover o destruidor do Carrinho
        #if self.request.session.get('carrinho'):
        #    del self.request.session['carrinho']
        #    self.request.session.save()

        http_referer = self.request.META.get(
            'HTTP_REFERER', 
            reverse('produto:lista')
            )
        variacao_id = self.request.GET.get('vid')
        if not variacao_id:
            messages.error(
                self.request,
                'Produto não encontrado !!!'
            )
            return redirect(http_referer) # URL anterior da Atual

        variacao = get_object_or_404(models.Variacao, id=variacao_id)

        if variacao.estoque < 1:
            messages.error(
                self.request,
                'Estoque insuficiente'
            )
            return redirect(http_referer) # URL anterior da Atual

        produto = variacao.produto
        produto_id = produto.id
        produto_nome = produto.nome
        variacao_nome = variacao.nome or ''
        preco_unitario = variacao.preco
        preco_unitario_promocional = variacao.preco_promocional
        quantidade = 1
        slug = produto.slug
        imagem = produto.imagem
        variacao_estoque = variacao.estoque

        if imagem:
            imagem = imagem.name
        else:
            imagem = ''

        if not self.request.session.get('carrinho'):
            self.request.session['carrinho'] = {}
            self.request.session.save()
        
        carrinho = self.request.session['carrinho']

        if variacao_id in carrinho:
            quantidade_carrinho = carrinho[variacao_id]['quantidade']
            quantidade_carrinho += 1

            if variacao_estoque < quantidade_carrinho:
                messages.warning(
                    self.request,
                    f'Estoque insuficiente para {quantidade_carrinho}x no produto {produto_nome}. '
                    f'Adicionamos {variacao_estoque}x no seu carrinho. '
                ) 
                quantidade_carrinho = variacao_estoque
                
            carrinho[variacao_id]['quantidade'] = quantidade_carrinho
            carrinho[variacao_id]['preco_quantitativo'] = preco_unitario * quantidade_carrinho
            carrinho[variacao_id]['preco_quantitativo_promocional'] = preco_unitario_promocional * quantidade_carrinho
        else:
            carrinho[variacao_id] = {
                'produto_id ': produto_id,
                'produto_nome': produto_nome, 
                'variacao_nome': variacao_nome,
                'variacao_id': variacao_id,
                'preco_unitario': preco_unitario,
                'preco_unitario_promocional': preco_unitario_promocional,
                'preco_quantitativo': preco_unitario,
                'preco_quantitativo_promocional': preco_unitario_promocional,
                'quantidade': 1,
                'slug': slug, 
                'imagem': imagem,  
            }
        
        self.request.session.save()
        messages.success(
            self.request,
            f'Produto {produto_nome} {variacao_nome} adicionado ao seu carrinho {carrinho[variacao_id]["quantidade"]}'
        )
        return redirect(http_referer)

class RemoverDoCarrinho(View):
    pass

class Carrinho(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'produto/carrinho.html')

class Finalizar(View):
    pass