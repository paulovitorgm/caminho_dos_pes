from django.shortcuts import render, redirect
from .formularios import Venda
from django.contrib import messages
from .models.registrar_venda import Registrar_venda
from .models.registrar_despesas import Registrar_despesa
from .formularios import Despesa


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


def registrar_venda(request):
    pass


    
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





def campo_vazio(campo):
    return not campo.strip()