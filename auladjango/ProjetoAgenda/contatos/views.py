from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.http import Http404
from django.db.models import Q, Value # para consultas mais complexas
from django.db.models.functions import Concat
from .models import Contato
from django.contrib import messages

# Create your views here.

def index(request):


    # contatos = Contato.objects.all()
    contatos = Contato.objects.order_by('nome').filter(
        mostrar=True
    ) # colocar (-) ele fica em ordem decrescente ex -nome

    paginator = Paginator(contatos, 2)  # Show 25 contacts per page

    page = request.GET.get('p')
    contatos = paginator.get_page(page)


    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })


def ver_contato(request, contato_id):
    # contato = Contato.objects.get(id=contato_id)
    contato = get_object_or_404(Contato, id=contato_id)
    if not contato.mostrar:
        raise Http404()
    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
    })


def busca(request):
    termo = request.GET.get('termo')

    """
    Consulta simples
    contatos = Contato.objects.order_by('nome').filter(
        nome=termo, 
        mostrar=True,
    )  # colocar (-) ele fica em ordem decrescente ex -nome
    """
    """
    Consulta tudo com And
    # icontains ver se uma parte do termo contém no campo nele
    contatos = Contato.objects.order_by('nome').filter(
        nome__icontains=termo,
        sobrenome__icontains=termo,
        mostrar=True,
    )  # colocar (-) ele fica em ordem decrescente ex -nome
    
    contatos = Contato.objects.order_by('nome').filter(
        Q(nome__icontains=termo) | Q(sobrenome__icontains=termo), # este ou Este = nome like %termo% or sobrenome like %termo%
        mostrar=True,
    )
    """
    campos = Concat('nome', Value(' '), 'sobrenome')

    if termo is None or not termo:
        messages.add_message(request, messages.ERROR, 'Campo termo não pode ser vazio.')
        return redirect('index')

    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo),
        mostrar=True,
    )
    paginator = Paginator(contatos, 2)  # Show 25 contacts per page

    page = request.GET.get('p')
    contatos = paginator.get_page(page)


    return render(request, 'contatos/busca.html', {
        'contatos': contatos
    })
