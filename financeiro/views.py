from django.shortcuts import render, redirect, get_list_or_404
from .formularios import Venda, Despesa
from django.contrib import messages
from .models.registrar_venda import Registrar_venda
from .models.registrar_despesas import Registrar_despesa
from django.core.paginator import Paginator


def registar_procedimento(request):
    if request.user.is_authenticated:
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
            registro_de_venda = Registrar_venda.objects.create(
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
    else:
        return redirect('login')
    
def registrar_despesa(request):
    if request.user.is_authenticated:
        despesa =  Despesa()
        contexto = {'despesa' : despesa}
        if request.method == 'POST':
            fornecedor = request.POST['fornecedor']
            data = request.POST['data']
            produtos = request.POST['produtos']
            total = request.POST['total']
            pagamento = request.POST['pagamento']
            observacoes = request.POST['observacoes']
            registro_de_despesa = Registrar_despesa.objects.create(
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
    else:
        return redirect('login')

def financas__entradas():
    lista_de_vendas = get_list_or_404(Registrar_venda.objects.filter().order_by('data'))
    return lista_de_vendas

def total_de_vendas():
    lista_entradas = Registrar_venda.objects.filter()
    total_vendas = sum(coluna.total for coluna in lista_entradas)
    return total_vendas

def entradas(request):
    if request.user.is_authenticated:
        entradas = financas__entradas()
        paginator_entradas = Paginator(entradas, 1)
        page = request.GET.get('page')
        linhas_por_pagina_entradas = paginator_entradas.get_page(page)

        contexto = {
            'entradas' : linhas_por_pagina_entradas,    
            'total_entradas': total_de_vendas(),
            }
        return render (request, 'entradas.html', contexto)
    else:
        return redirect('login')

def financas__despesas():
    lista_de_despesas = get_list_or_404(Registrar_despesa.objects.filter().order_by('data'))
    return lista_de_despesas

def total_de_despesas():
    lista_despesas = Registrar_despesa.objects.filter()
    total_despesas = sum(coluna.total for coluna in lista_despesas)
    return total_despesas

def campo_vazio(campo):
    return not campo.strip()

def saidas(request):
    if request.user.is_authenticated:
        saidas = financas__despesas()
        page = request.GET.get('page')
        paginator_saidas = Paginator(saidas, 2)
        linhas_por_pagina_saidas = paginator_saidas.get_page(page)
        contexto = {
            'saidas' : linhas_por_pagina_saidas,
            'total_despesas': total_de_despesas()
            }
        return render (request, 'saidas.html', contexto)
    else:
        return redirect('login')