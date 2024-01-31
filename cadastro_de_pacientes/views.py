from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from cadastro_de_pacientes.forms.cadastro_de_pacientes import CadastroDePacienteForm
from cadastro_de_pacientes.forms.anamnese import AnamneseForm
from cadastro_de_pacientes.forms.busca import BuscaForm
from cadastro_de_pacientes.models.cadastro_pacientes import CadastroDePaciente


@login_required(login_url='login')
def cadastro_de_pacientes(request):
    form = CadastroDePacienteForm()
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
            return redirect('busca')
    contexto = {'form': form}
    return render(request, 'cadastro_de_pacientes/cadastro_de_pacientes.html', contexto)


@login_required(login_url='login')
def busca(request):
    form = BuscaForm
    contexto = {'form': form}
    if 'busca' in request.GET:
        nome_a_buscar = request.GET['busca']
        lista_de_pacientes = CadastroDePaciente.objects.filter(nome_paciente__icontains=nome_a_buscar.split()[0])

        if lista_de_pacientes:
            messages.success(request, 'Pacientes encontrados:')
            contexto = {'form': form,
                        'busca': lista_de_pacientes}
        else:
            messages.error(request,'Nenhum paciente encontrado, tente novamente.')
        return render(request, 'busca.html', contexto)

    return render(request, 'busca.html', contexto)


@login_required(login_url='login')
def salvar_anamnese(request, anamnese_id):
    paciente = AnamneseForm()
    contexto = {'form': paciente, 'anamnese_id': anamnese_id}
    return render(request, 'busca.html', contexto)


@login_required(login_url='login')
def anamnese(request, paciente_id):
    form = AnamneseForm()


    contexto = {'form': form}

    return render(request, 'cadastro_de_pacientes/anamnese.html', contexto)

