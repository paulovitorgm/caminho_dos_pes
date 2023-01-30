from django import forms
from django.forms.widgets import DateInput
from .models.registrar_venda import Registrar_venda
from .models.registrar_despesas import Registrar_despesa



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
        

class Despesa(forms.ModelForm):
    fornecedor = forms.CharField(label='Nome do fornecedor', widget=forms.TextInput(attrs={'placeholder':'Ex: Potus hospitalar'}))
    data = forms.DateField(label='Data da compra', widget=forms.DateInput(attrs={'type':'date'}))
    produtos = forms.CharField(label='Produtos', widget=forms.TextInput(attrs={'placeholder':'Ex: Mille extreme'}))
    total = forms.DecimalField(label='Valor total', max_digits=10,decimal_places=2, min_value=0, widget=forms.NumberInput(attrs={'placeholder':'Ex: 100,00'}))
    meios_de_pagamento = [('cred','Crédito'),('deb','Débito'),('pix','Pix'), ('din', 'Dinheiro')]
    pagamento = forms.ChoiceField(label='Forma de pagamento', choices=meios_de_pagamento)
    observacoes = forms.CharField(label='Observações', required=False, widget=forms.Textarea(attrs={'placeholder':'Ex: Produto "x" mudou a composição.'}))

    class Meta:
        model = Registrar_despesa
        exclude = ['']