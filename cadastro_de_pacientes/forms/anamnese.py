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

    diabetico = forms.CharField(label="Diabético",
                                widget=forms.ChoiceField(choices=escolha,
                                                         initial='Não',
                                                         attrs={'class': 'form-control'}))

    hepatite = forms.CharField(label="Hepatite",
                               widget=forms.ChoiceField(choices=escolha,
                                                         initial='Não',
                                                         attrs={'class': 'form-control'}))

    hiv = forms.CharField(label="Hepatite",
                          widget=forms.ChoiceField(choices=escolha,
                                                   initial='Não',
                                                   attrs={'class': 'form-control'}))
    gravidez = forms.CharField(label="Está gestante?",
                               widget=forms.ChoiceField(choices=escolha,
                                                        initial='Não',
                                                        attrs={'class': 'form-control'}))

    lactante = forms.CharField(label="Está amamentando?",
                               widget=forms.ChoiceField(choices=escolha,
                                                        initial='Não',
                                                        attrs={'class': 'form-control'}))

    hipertensao = forms.CharField(label="Hipertensão",
                                  widget=forms.ChoiceField(choices=escolha,
                                                           initial='Não',
                                                           attrs={'class': 'form-control'}))

    hipotensao = forms.CharField(label="Hipotensão",
                                 widget=forms.ChoiceField(choices=escolha,
                                                          initial='Não',
                                                          attrs={'class': 'form-control'}))

    observacoes = forms.CharField(label="Já teve câncer? Qual?",
                                  max_length=50,
                                  widget=forms.Textarea(attrs={'class': 'form-control',
                                                               'autocomplete': 'off',
                                                               'oninput': 'receber_apenas_letras(this)'}))
    class Meta:
        model = Anamnese
        fields = '__all__'
