import imp
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
# Create your views here.


class ListaProdutos(ListView):
    # USANDO PARA TESTE
    def get(self, *args, **kwargs):
        return HttpResponse('pAGAR')

class DetalheProdutos(View):
    pass

class AdicionarAoCarrinho(View):
    pass

class RemoverDoCarrinho(View):
    pass

class Carrinho(View):
    pass

class Finalizar(View):
    pass