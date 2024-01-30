from django import forms
from django.core.exceptions import ValidationError

from cadastro_de_pacientes.models.cadastro_pacientes import CadastroDePaciente
from apps.materiais_em_comum import lista_caracteres


class BuscaForm(forms.Form):
    busca = forms.CharField(label='Nome do paciente',
                                    max_length=200,
                                    strip=True,
                                    widget=forms.TextInput(attrs={'placeholder': 'Ex: Paulo',
                                                                  'autocomplete': 'off',
                                                                  'class': 'form-control',
                                                                  'oninput': 'receber_apenas_letras(this)'}))

    class Meta:
        model = CadastroDePaciente
        fields = ['nome_paciente']

    def clean_busca(self):
        busca = self.cleaned_data.get("nome_paciente")
        for i in busca:
            if i in lista_caracteres:
                raise ValidationError(f'O caractere {i} é inválido.')
        return busca
