from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from usuarios.forms import EditaUsuarioForm
from usuarios.forms.login import LoginForm
from usuarios.forms.cadastrar_usuario import UsuarioForm


def fazer_login(request):
    if request.user.is_authenticated:
        messages.error(request, 'Você já fez login.')
        return redirect('dashboard')
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            messages.success(request, "Login realizado com sucesso.")
            return redirect("index")
        else:
            messages.error(request, "Erro ao fazer login, tente novamente.")

    contexto = {'form': form}
    return render(request, 'registration/login.html', contexto)


@login_required(login_url='login')
def fazer_logout(request):
    logout(request)
    return redirect('index')


def criar_usuario(request):
    if request.user.is_authenticated:
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


@login_required(login_url='login')
def editar_usuario(request):
    form = EditaUsuarioForm(instance=request.user)
    contexto = {'form': form}

    if request.method == 'POST':
        form = EditaUsuarioForm(request.POST, instance=request.user)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Usuario alterado com sucesso")
                return redirect('index')
            except (IntegrityError, ValidationError) as e:
                messages.error(request, f'Erro ao editar usuário: {e}')
                return redirect('editar_usuario')

    return render(request, 'registration/editar_usuario.html', contexto)
