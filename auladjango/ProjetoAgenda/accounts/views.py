from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.


def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    usuario = request.POST.get('txtUsuario')
    senha = request.POST.get('txtSenha')

    user = auth.authenticate(request, username=usuario, password=senha)
    if not user:
        messages.error(request, 'Usuário ou senha inválida.')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Login efetuado com sucesso. ')
        return redirect('dashboard')


def logout(request):
    auth.logout(request)
    return redirect('login')


def cadastro(request):
    if request.method != 'POST':
        return render(request, 'accounts/cadastro.html')

    nome = request.POST.get('txtNome')
    sobrenome = request.POST.get('txtSobrenome')
    email = request.POST.get('txtEmail')
    usuario = request.POST.get('txtUsuario')
    senha = request.POST.get('txtSenha')
    repetirSenha = request.POST.get('txtRepetirSenha')

    if not nome or not sobrenome or not email or not usuario or not senha or not repetirSenha:
        messages.error(request, 'Nenhum campo pode estar vazio.')
        return render(request, 'accounts/cadastro.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'Email inválido.')
        return render(request, 'accounts/cadastro.html')


    if len(usuario) < 6:
        messages.error(request, 'Usuário precisa term 6 caracteres ou mais.')
        return render(request, 'accounts/cadastro.html')

    if len(senha) < 6:
        messages.error(request, 'Senha precisa term 6 caracteres ou mais.')
        return render(request, 'accounts/cadastro.html')

    if senha != repetirSenha:
        messages.error(request, 'Senha diferente de Repetir senha.')
        return render(request, 'accounts/cadastro.html')

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Usuário já existe.')
        return render(request, 'accounts/cadastro.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'Email já existe.')
        return render(request, 'accounts/cadastro.html')

    messages.success(request, 'Registado com sucesso! \n Agora Faça login ')

    user = User.objects.create_user(username=usuario, email=email, password=senha, first_name=nome, last_name=sobrenome)
    user.save()
    return redirect('login')


@login_required(redirect_field_name='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

