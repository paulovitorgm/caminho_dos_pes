from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .formulario import UsuarioForm


def fazer_login(request):
    if request.user.is_authenticated:
        messages.error(request, 'Você já fez login.')
        return redirect('dashboard')
    if request.method == 'POST':
        usuario = request.POST['email']
        senha = request.POST['senha']

        if campo_vazio(usuario) or campo_vazio(senha):
            messages.error(request, 'Os campos email e senha não podem ficar em branco.')
            return redirect('login')

        user = authenticate(request, username=usuario, password=senha)

        if user is None:
            messages.error(request, "Usuário ou senha inválidos.")
            return redirect('login')

        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'login.html')


@login_required(login_url='login')
def fazer_logout(request):
    logout(request)
    return redirect('index')


def criar_usuario(request):
    if verifica_se_logado(request):
        messages.error(request, 'Você já fez login.')
        return redirect('index')
    form = UsuarioForm()
    if request.method == 'POST':
        form = UsuarioForm(request.POST)

        if form.is_valid():
            usuario = User.objects.create_user(username=request.POST['username'],
                                               email=request.POST['email'],
                                               password=request.POST["password"],
                                               first_name=request.POST['first_name'],
                                               last_name=request.POST['last_name'])
            usuario.save()
            return redirect('login')

    contexto = {'form': form}
    return render(request, 'criar_usuario.html', contexto)


def campo_vazio(campo):
    return not campo.strip()


def verifica_se_logado(request):
    return request.user.is_authenticated
