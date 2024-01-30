from django import forms
from django.core.exceptions import ValidationError

from cadastro_de_pacientes.models.cadastro_pacientes import CadastroDePaciente
from apps.materiais_em_comum import lista_caracteres, sexo_op

from datetime import timedelta, date

class CadastroDePacienteForm(forms.ModelForm):
    nome_paciente = forms.CharField(label='Nome do paciente',
                                    max_length=200,
                                    strip=True,
                                    widget=forms.TextInput(attrs={'placeholder': 'Ex: Paulo',
                                                                  'autocomplete': 'off',
                                                                  'class': 'form-control',
                                                                  'oninput': 'receber_apenas_letras(this)'}))

    sobrenome_paciente = forms.CharField(label='Sobrenome do paciente',
                                         max_length=200,
                                         strip=True,
                                         widget=forms.TextInput(attrs={'placeholder': 'Ex: da Silva',
                                                                       'autocomplete': 'off',
                                                                       'class': 'form-control',
                                                                       'oninput': 'receber_apenas_letras(this)'}))

    telefone = forms.CharField(label='Telefone',
                               max_length=11,
                               widget=forms.TextInput(attrs={'placeholder': '(XX) XXXXX-XXXX',
                                                             'autocomplete': 'off',
                                                             'class': 'form-control',
                                                             'oninput': 'receber_apenas_numeros(this)'}))

    primeiro_atendimento = forms.DateField(label='Data do primeiro atendimento',
                                           required=False,
                                           widget=forms.DateInput(attrs={'type': 'date',
                                                                         'autocomplete': 'off',
                                                                         'class': 'form-control'}), )

    email = forms.CharField(label='E-mail',
                             max_length=150,
                             strip=True,
                             required=False,
                             widget=forms.EmailInput(attrs={'placeholder': 'email@email.com',
                                                            'autocomplete': 'off',
                                                            'class': 'form-control'}))

    sexo = forms.ChoiceField(label='Sexo',
                             choices=sexo_op,
                             widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = CadastroDePaciente
        fields = "__all__"

    def clean_nome_paciente(self):
        nome = self.cleaned_data.get("nome_paciente")
        for i in nome:
            if i in lista_caracteres:
                raise ValidationError(f'O caractere {i} é inválido.')
        return nome

    def clean_sobrenome_paciente(self):
        sobrenome = self.cleaned_data.get("sobrenome_paciente")
        for i in sobrenome:
            if i in lista_caracteres:
                raise ValidationError(f'O caractere {i} é inválido.')
        return sobrenome

    def clean_telefone(self):
        telefone = self.cleaned_data.get("telefone")
        for i in telefone:
            if not i.isnumeric():
                raise ValidationError(f'O caractere {i} é inválido.')
        return telefone

    def clean_primeiro_atendimento(self):
        data = self.cleaned_data.get("primeiro_atendimento")
        if data > date.today():
            raise ValidationError(f'A data não pode ser posterior ao dia de hoje.')
        return data
