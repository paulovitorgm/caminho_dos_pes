from django.shortcuts import render, redirect
from . formularios import Cadastro_de_paciente
from django.contrib.auth.models import User
from django.contrib import messages


def cadastro_de_pacientes(request):
   forms = Cadastro_de_paciente()
   contexto = {
       'cadastro_de_pacientes' : forms 
   }
   if request.method == 'POST':
      nome_paciente = request.POST['nome_paciente']
      sobrenomenome_paciente = request.POST['sobrenome_paciente']
      telefone = request.POST['telefone']
      primeiro_atendimento = request.POST['primeiro_atendimento']
      email = request.POST['email']
      foto = request.FILES['foto']
      nome_completo = request.POST['nome_completo']
      if paciente_ja_existe(telefone):
         messages.error(request, 'O paciente já está cadastrado.')
         return redirect('')  
   # FALTA CONTEÚDO


   def paciente_ja_existe(telefone):
      '''Verifica no banco de dados, usando o telefone completodo, se o paciente existe'''
      return User.objects.filter(telefone=telefone).exists()

   return render(request,'cadastro_de_pacientes.html', contexto)
