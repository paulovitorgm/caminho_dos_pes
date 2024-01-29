from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from apps.materiais_em_comum import lista_caracteres


class EditaUsuarioForm(forms.ModelForm):
    first_name = forms.CharField(label='Nome',
                                 strip=True,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'Ex: José',
                                                               'class': 'form-control',
                                                               'autocomplete': 'off',
                                                               'oninput': 'receber_apenas_letras(this)'}))

    last_name = forms.CharField(label='Sobrenome',
                                strip=True,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Ex: da Silva',
                                                              'class': 'form-control',
                                                              'autocomplete': 'off',
                                                              'oninput': 'receber_apenas_letras(this)'}))

    email = forms.EmailField(label='Email',
                             required=True,
                             widget=forms.EmailInput(attrs={'placeholder': 'jose@gmail.com',
                                                            'class': 'form-control',
                                                            'autocomplete': 'off'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def clean_first_name(self):
        nome = self.cleaned_data.get('first_name')
        for i in nome:
            if i in lista_caracteres:
                raise ValidationError(f'O caractere {i} é inválido.')
        return nome

    def clean_last_name(self):
        sobrenome = self.cleaned_data.get('last_name')
        for i in sobrenome:
            if i in lista_caracteres:
                raise ValidationError(f'O caractere {i} é inválido.')
        return sobrenome

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise ValidationError('Email já cadastrado')
        return email

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
