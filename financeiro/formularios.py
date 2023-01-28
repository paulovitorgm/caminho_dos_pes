from django import forms
from django.forms.widgets import DateInput
from .models.registrar_venda import Registrar_venda
from .models.registrar_fornecedores import Registrar_fornecedor



class Venda(forms.ModelForm):
    data = forms.DateField(label='Data do atendimento',widget=DateInput(attrs={'type':'date'}))
    paciente = forms.CharField(label='Nome do paciente',widget=forms.TextInput(attrs={'placeholder':'Ex: Paulo Vitor'}))
    servico = forms.CharField(label = 'Serviço realizado',widget=forms.TextInput(attrs={'placeholder':'Ex: Assepsia completa'}),required=False)
    produtos = forms.CharField(label='Produtos',widget=forms.TextInput(attrs={'placeholder':'Ex: FungiPro'}),required=False)
    total = forms.DecimalField(label='Valor total',max_digits=10, decimal_places=2,min_value=0,widget=forms.NumberInput(attrs={'placeholder':'Ex: 100,00'}))
    meios_de_pagamento = [('cred','Crédito'),('deb','Débito'),('pix','Pix'), ('din', 'Dinheiro')]
    pagamento = forms.ChoiceField(label='Forma de pagamento',choices=meios_de_pagamento)

    class Meta:
        model = Registrar_venda
        exclude = ['']
        



class Fornecedor(forms.ModelForm):
    cnpj = forms.CharField(label='CNPJ',required=False, widget=forms.TextInput({'placeholder':'XX. XXX. XXX/0001-XX'}),max_length=14)
    razao_social = forms.CharField(label='Razão social', widget=forms.TextInput(attrs={'placeholder':'Ex: Coca Cola Indústrias Ltda'}),max_length=150)
    nome_fantasia = forms.CharField(label='Nome fantasia', widget=forms.TextInput(attrs={'placeholder':'Ex: Coca Cola'}),max_length=100)
    telefone = forms.CharField(label='Telefone', widget=forms.TextInput(attrs={'placeholder':'(XX) XXXXX-XXXX'}),max_length=11)

    class Meta:
        model = Registrar_fornecedor
        exclude = ['']