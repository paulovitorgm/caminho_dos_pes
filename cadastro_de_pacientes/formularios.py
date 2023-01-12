from django import forms
from datetime import datetime

#instalar e importar o tempus dominus  - DatePicker
#from tempus_dominus.widgets import DatePicker


class Cadastro_de_paciente(forms.Form):
    nome_paciente = forms.CharField(label='Nome do paciente', max_length=200)
    telefone = forms.CharField(label='Telefone', max_length=11)
    primeiro_atendimento = forms.DateField(disabled=True ,initial=datetime.today)
    nome_paciente = forms.CharField(label='Nome do paciente', max_length=200)
# nome
# telefone
# primeiro atendimento em
# email
# data de nascimento