from django.shortcuts import render, redirect, get_list_or_404
from .formularios import Venda, Despesa
from django.contrib import messages
from .models.registrar_venda import RegistrarVenda
from .models.registrar_despesas import RegistrarDespesa
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def registar_procedimento(request):
    vendas = Venda()
    contexto = {'venda':vendas}
    if request.method == 'POST':
        data = request.POST['data']
        paciente = request.POST['paciente']
        if campo_vazio(paciente):
            messages.error(request, 'O nome do paciente não pode ficar em branco.')
            return redirect('registrar_procedimento')
        servico = request.POST['servico']
        produtos = request.POST['produtos']
        total = request.POST['total']            
        pagamento = request.POST['pagamento']
        registro_de_venda = RegistrarVenda.objects.create(
            data = data,
            paciente = paciente,
            servico = servico,
            produtos = produtos,
            total = total,
            pagamento = pagamento
        )
        registro_de_venda.save()
        messages.success(request,'Venda registrada com sucesso.')
        return redirect('registrar_procedimento')
    else:
        return render(request, 'registrar_procedimentos.html', contexto)

    
@login_required(login_url='login')
def registrar_despesa(request):
    despesa =  Despesa()
    contexto = {'despesa' : despesa}
    if request.method == 'POST':
        fornecedor = request.POST['fornecedor']
        data = request.POST['data']
        produtos = request.POST['produtos']
        total = request.POST['total']
        pagamento = request.POST['pagamento']
        observacoes = request.POST['observacoes']
        registro_de_despesa = RegistrarDespesa.objects.create(
            fornecedor = fornecedor,
            data = data,
            produtos = produtos,
            total = total,
            pagamento = pagamento,
            observacoes = observacoes,
        )
        registro_de_despesa.save()
        messages.success(request, 'Despesa registrada com sucesso.')
        return redirect('registrar_despesa')
    return render (request, 'registrar_despesa.html',contexto)


def financas__entradas(request):
    if request.method == "GET":
        lista_de_vendas = filtro_de_data_entradas(request)
    else:
        lista_de_vendas = get_list_or_404(RegistrarVenda.objects.filter().order_by('data'))
    return lista_de_vendas


def total_de_vendas(request):
    lista_entradas =  filtro_de_data_entradas(request)
    total_vendas = sum(coluna.total for coluna in lista_entradas)
    return total_vendas



@login_required(login_url='login')
def entradas(request):
    entradas = financas__entradas(request)
    paginator_entradas = Paginator(entradas, 10)
    page = request.GET.get('page')
    linhas_por_pagina_entradas = paginator_entradas.get_page(page)
    contexto = {
        'entradas' : linhas_por_pagina_entradas,    
        'total_entradas': total_de_vendas(request),
        }
    return render (request, 'entradas.html', contexto)


def filtro_de_data_entradas(request):
    data_inicial = request.GET.get('data_inicial')
    data_final = request.GET.get('data_final')
    if data_inicial and data_final:
        filtro = get_list_or_404(RegistrarVenda.objects.filter(data__range=[data_inicial,data_final]))
        return filtro
    else:
        return get_list_or_404(RegistrarVenda.objects.all())


def financas__despesas(request):
    if request.method == "GET":
        lista_de_despesas = filtro_de_data_saidas(request)
    else:
        lista_de_despesas = get_list_or_404(RegistrarDespesa.objects.filter().order_by('data'))
    return lista_de_despesas

def total_de_despesas(request):
    lista_despesas = filtro_de_data_saidas(request)
    total_despesas = sum(coluna.total for coluna in lista_despesas)
    return total_despesas

@login_required(login_url='login')
def saidas(request):
    saidas = financas__despesas(request)
    page = request.GET.get('page')
    paginator_saidas = Paginator(saidas, 10)
    linhas_por_pagina_saidas = paginator_saidas.get_page(page)
    contexto = {
        'saidas' : linhas_por_pagina_saidas,
        'total_despesas': total_de_despesas(request)
        }
    return render (request, 'saidas.html', contexto)
    

def filtro_de_data_saidas(request):
    data_inicial = request.GET.get('data_inicial')
    data_final = request.GET.get('data_final')
    if data_inicial and data_final:
        filtro = filtro = get_list_or_404(RegistrarDespesa.objects.filter(data__range=[data_inicial,data_final]))
        return filtro
    else:
        return  get_list_or_404(RegistrarDespesa.objects.all())


def campo_vazio(campo):
    return not campo.strip()
