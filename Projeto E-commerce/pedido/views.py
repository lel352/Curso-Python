from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse


# Create your views here.

class Pagar(View):
    # USANDO PARA TESTE
    def get(self, *args, **kwargs):
        return HttpResponse('pAGAR')
    

class SalvarPedido(View):
    pass

class Detalhe(View):
    pass