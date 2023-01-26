from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages



def index(request):
   return render(request, 'index.html')

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
      user = authenticate(request, username = usuario, password = senha)
      
      if user is not None:
         login(request, user)
         return redirect ('index')

   return render(request,'login.html')


def fazer_logout(request):
   logout(request)
   return redirect('index')

def criar_usuario(request):
   verifica_se_logado(request)
   if request.method =='POST':
      nome = request.POST['nome']
      sobrenome = request.POST['sobrenome']
      email = request.POST['email']
      if usuario_existente(email):
         messages.error(request, 'Email já cadastrado.')
         return redirect('login')      
      senha = request.POST['senha']
      senha2 = request.POST['senha2']    
      if  senhas_sao_diferentes(senha, senha2):
         messages.error(request, 'As senhas não são iguais.')
         return redirect('criar_usuario')

      usuario = User.objects.create_user(username=email, email=email, password=senha)
      usuario.first_name = nome
      usuario.last_name = sobrenome
      usuario.save()

      return redirect ('login')
   return render(request,'criar_usuario.html')







def campo_vazio(campo):
    return not campo.strip()

def verifica_se_logado(request):
   if request.user.is_authenticated:
      messages.error(request, 'Você já fez login.')
      return redirect('index')

def senhas_sao_diferentes(senha, senha2):
   return senha != senha2

def usuario_existente(email):
    return User.objects.filter(email=email).exists()