from django import forms

from cadastro_de_pacientes.models import Anamnese
from apps.materiais_em_comum import escolha


class AnamneseForm(forms.ModelForm):
    acompanhamento_medico = forms.CharField(label="Faz acompanhamento médico? Qual?",
                                            max_length=50,
                                            widget=forms.TextInput(attrs={'placeholder': 'Não faz',
                                                                          'class': 'form-control',
                                                                          'autocomplete': 'off',
                                                                          'oninput': 'receber_apenas_letras(this)'}))

    medicamento_em_uso = forms.CharField(label="Faz uso de medicação? Qual?",
                                         max_length=50,
                                         widget=forms.TextInput(attrs={'placeholder': 'Não faz',
                                                                       'class': 'form-control',
                                                                       'autocomplete': 'off',
                                                                       'oninput': 'receber_apenas_letras(this)'}))

    alergico = forms.CharField(label="Tem alegria? Qual?",
                               max_length=50,
                               widget=forms.TextInput(attrs={'placeholder': 'Não faz',
                                                             'class': 'form-control',
                                                             'autocomplete': 'off',
                                                             'oninput': 'receber_apenas_letras(this)'}))

    teve_cancer = forms.CharField(label="Já teve câncer? Qual?",
                                  max_length=50,
                                  widget=forms.TextInput(attrs={'placeholder': 'Não faz',
                                                                'class': 'form-control',
                                                                'autocomplete': 'off',
                                                                'oninput': 'receber_apenas_letras(this)'}))

    diabetico = forms.ChoiceField(label='Tem diabetes?',
                                  choices=escolha,
                                  widget=forms.Select(attrs={'class': 'form-select'}))

    hepatite = forms.ChoiceField(label='Tem hepatite?',
                                  choices=escolha,
                                  widget=forms.Select(attrs={'class': 'form-select'}))


    hiv = forms.ChoiceField(label='Tem HIV?',
                                  choices=escolha,
                                  widget=forms.Select(attrs={'class': 'form-select'}))

    gravidez = forms.ChoiceField(label='Está gestante?',
                                  choices=escolha,
                                  widget=forms.Select(attrs={'class': 'form-select'}))

    lactante = forms.ChoiceField(label='Está amamentando?',
                                  choices=escolha,
                                  widget=forms.Select(attrs={'class': 'form-select'}))

    hipertensao = forms.ChoiceField(label='Tem hipertensão?',
                                    choices=escolha,
                                    widget=forms.Select(attrs={'class': 'form-select'}))

    hipotensao = forms.ChoiceField(label='Tem hipotensão?',
                                   choices=escolha,
                                   widget=forms.Select(attrs={'class': 'form-select'}))

    observacoes = forms.CharField(label="Já teve câncer? Qual?",
                                  max_length=400,
                                  widget=forms.Textarea(attrs={'class': 'form-control',
                                                               'autocomplete': 'off',
                                                               'oninput': 'receber_apenas_letras(this)'}))

    class Meta:
        model = Anamnese
        fields = '__all__'
