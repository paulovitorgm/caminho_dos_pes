from django.shortcuts import render, redirect, get_object_or_404
from . formularios import Cadastro_de_paciente
from .models.cadastro_pacientes import Cadastro_de_paciente as Cadastro
from . formularios import Anamnese
from . models.anamnese import Anamnese as Cadastrar_anamnese
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# from django.contrib.auth.decorators import login_required   
#  DESENVOLVER  

def index(request):
   return render(request, 'index.html')


def cadastro_de_pacientes(request):
   if request.user.is_authenticated:
      formulario = Cadastro_de_paciente()
      contexto = {'cadastro_de_pacientes' : formulario}
      
      if request.method == 'POST':
         nome_paciente = request.POST['nome_paciente']
         sobrenome_paciente = request.POST['sobrenome_paciente']
         telefone = request.POST['telefone']
         primeiro_atendimento = request.POST['primeiro_atendimento']
         email = request.POST['email']
         sexo = request.POST['sexo']
         if paciente_existente(telefone):
            messages.error(request,'Paciente já cadastrado.')
            return redirect('cadastro')
         else:
            paciente = Cadastro.objects.create(
               nome_paciente = nome_paciente,
               sobrenome_paciente = sobrenome_paciente,
               telefone = telefone,
               primeiro_atendimento = primeiro_atendimento,
               email = email,
               sexo = sexo
            )
            paciente.save()
            paciente_anamnese = Cadastrar_anamnese.objects.create(paciente=paciente)
            messages.success(request, 'Paciente cadastrado com sucesso.')
            contexto = {
               'paciente' : paciente,
               'anamnese' : paciente_anamnese
            }
            return redirect('cadastro')

      return render(request, 'cadastro_de_pacientes.html', contexto)   
   else:
      return redirect('login')



def busca(request):
   if request.user.is_authenticated:
      lista_de_pacientes = Cadastro.objects.order_by('nome_paciente')
      if 'busca' in request.GET:
         nome_a_buscar = request.GET['busca']
         if nome_a_buscar:
            lista_de_pacientes = lista_de_pacientes.filter(nome_paciente__icontains = nome_a_buscar)
            contexto = {'busca': lista_de_pacientes}
            return render(request, 'busca.html',contexto)
      else:
          return render(request, 'busca.html')
   else:
      return redirect('login')

def ver_anamnese(request):
   if request.user.is_authenticated:
      if request.method == 'POST':
         acompanhamento_medico = request.POST['acompanhamento_medico']
         especialidade = request.POST['especialidade']
         uso_medicacao = request.POST['uso_medicacao']
         medicamento_em_uso = request.POST['medicamento_em_uso']
         diabetico = request.POST['diabetico']
         hepatite = request.POST['hepatite']
         hiv = request.POST['hiv']
         problemas_circulatorios = request.POST['problemas_circulatorios']
         alergico = request.POST['alergico']
         alergia_a = request.POST['alergia_a']
         teve_cancer = request.POST['teve_cancer']
         tipo_cancer = request.POST['tipo_cancer']
         gravidez = request.POST['gravidez']
         lactante = request.POST['lactante']
         hipertensao = request.POST['hipertensao']
         hipotensao = request.POST['hipotensao']
         observacoes = request.POST['observacoes']
         
         paciente = Cadastrar_anamnese.objects.update(
            acompanhamento_medico = acompanhamento_medico,
            especialidade = especialidade,
            uso_medicacao = uso_medicacao,
            medicamento_em_uso = medicamento_em_uso,
            diabetico = diabetico,
            hepatite = hepatite,
            hiv = hiv,
            problemas_circulatorios = problemas_circulatorios,
            alergico = alergico,
            alergia_a = alergia_a,
            teve_cancer = teve_cancer,
            tipo_cancer = tipo_cancer,
            gravidez = gravidez,
            lactante = lactante,
            hipertensao = hipertensao,
            hipotensao = hipotensao,
            observacoes = observacoes
         )

         paciente = Cadastrar_anamnese.objects.get()

         messages.success(request, 'Anamnese cadastrada.')
         contexto = {'paciente' : paciente}

         return render(request, 'ver_anamnese.html', contexto)
   else:
      return redirect('login')


def preencher_anamnese(request):
   if request.user.is_authenticated:
      formulario = Anamnese()
      if request.method == 'GET':
         id_paciente = request.GET['id_paciente']
         paciente = Cadastrar_anamnese.objects.get(paciente_id = id_paciente)
         nome_paciente = Cadastro.objects.get(id = id_paciente)
         contexto = {'anamnese' : formulario,
                     'nome' : nome_paciente,
                     'paciente' : paciente
                     }
         return render(request, 'anamnese.html', contexto)
      else:
         return redirect('busca')
   else:
      return redirect('login')



def criar_usuario(request):
   verifica_se_logado(request)
   if request.method =='POST':
      nome = request.POST['nome']
      sobrenome = request.POST['sobrenome']
      email = request.POST['email']
      senha = request.POST['senha']
      senha2 = request.POST['senha2']
      usuario.first_name = nome
      usuario.last_name = sobrenome
      
      if  senhas_sao_diferentes(senha, senha2):
         messages.error(request, 'As senhas não são iguais.')
         return redirect('criar_usuario')
      
      if usuario_existente(email):
         messages.error(request, 'Email já cadastrado.')
         return redirect('criar_usuario')
      

      usuario = User.objects.create_user(username=email, email=email, password=senha)
      usuario.save()
      return redirect ('index')
   return render(request,'criar_usuario.html')




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

def paciente_existente(telefone):
   return Cadastro.objects.filter(telefone=telefone).exists()