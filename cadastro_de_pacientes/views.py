from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from cadastro_de_pacientes.forms.cadastro_de_pacientes import CadastroDePacienteForm
from cadastro_de_pacientes.forms.anamnese import AnamneseForm
from cadastro_de_pacientes.models.cadastro_pacientes import CadastroDePaciente


@login_required(login_url='login')
def cadastro_de_pacientes(request):
    if request.method == 'POST':
        form = CadastroDePacienteForm(request.POST)
        if form.is_valid():
            paciente = CadastroDePaciente.objects.create(
                    nome_paciente=request.POST['nome_paciente'],
                    sobrenome_paciente=request.POST['sobrenome_paciente'],
                    telefone=request.POST['telefone'],
                    primeiro_atendimento=request.POST['primeiro_atendimento'],
                    email=request.POST['email'],
                    sexo=request.POST['sexo'])

            paciente.save()
            messages.success(request, f'Paciente {request.POST["nome_paciente"]} cadastrado com sucesso.')
            return redirect('index')
        else:
            messages.error(request, f'Erro ao cadastrar paciente. Tente novamente.')
            return redirect(reverse('cadastro_de_pacientes'))
    form = CadastroDePacienteForm()
    contexto = {'form': form}
    return render(request, 'cadastro_de_pacientes/cadastro_de_pacientes.html', contexto)


@login_required(login_url='login')
def busca(request):
    lista_de_pacientes = CadastroDePaciente.objects.get().order_by('nome_paciente')
    if 'busca' in request.GET:
      nome_a_buscar = request.GET['busca']
      if nome_a_buscar:
         lista_de_pacientes = lista_de_pacientes.filter(nome_paciente__icontains = nome_a_buscar)
         contexto = {'busca': lista_de_pacientes}
         if lista_de_pacientes:
            messages.success(request, 'Pacientes encontrados:')
         else:
            messages.error(request,'Nenhum paciente encontrado, tente novamente.')
         return render(request, 'busca.html', contexto)
    else:
         return render(request, 'busca.html')


@login_required(login_url='login')
def salvar_anamnese(request, anamnese_id):
    paciente = AnamneseForm()

    return render(request, 'busca.html')


@login_required(login_url='login')
def anamnese(request):
    return render(request, 'cadastro_de_pacientes/anamnese.html')


def campo_vazio(campo):
    return not campo.strip()


def verifica_se_logado(request):
    if request.user.is_authenticated:
        messages.error(request, 'Você já fez login.')
        return redirect('dashboard')


def senhas_sao_diferentes(senha, senha2):
    return senha != senha2


def usuario_existente(email):
    return User.objects.filter(email=email).exists()


def verifica_se_somente_numeros(campo):
    return not campo.isnumeric()
