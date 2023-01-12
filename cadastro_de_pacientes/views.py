from django.shortcuts import render
from . formularios import Cadastro_de_paciente


def cadastro_de_pacientes(request):
    forms = Cadastro_de_paciente()
    contexto = {
       'cadastro_de_pacientes' : forms 
    }
    return render(request,'cadastro_de_pacientes.html', contexto)
