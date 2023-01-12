from django import forms
from datetime import datetime


class Cadastro_de_paciente(forms.Form):
    nome_paciente = forms.CharField(label='Nome do paciente', max_length=200)
    sobrenome_paciente = forms.CharField(label='Sobrenome do paciente', max_length=200)
    telefone = forms.CharField(label='Telefone', max_length=11)
    primeiro_atendimento = forms.DateField(disabled=True ,initial=datetime.today)
    email = forms.EmailField(label='Email', max_length=200)
    foto = forms.FileField(label='Foto', required=False)
    nome_completo = nome_paciente, sobrenome_paciente
    nome_completo = forms.CharField(label='nome completo', initial=nome_completo)

   
    # def __str__(self):
    #     return self.nome_paciente, self.sobrenome_paciente