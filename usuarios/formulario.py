from django import forms

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UsuarioForm(forms.ModelForm):
    first_name = forms.CharField(label='Nome',
                                 strip=True,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'Ex: José',
                                                         'class': 'form-control',
                                                         'autocomplete': 'off'}))

    last_name = forms.CharField(label='Sobrenome',
                                strip=True,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Ex: da Silva',
                                                              'class': 'form-control',
                                                              'autocomplete': 'off'}))

    username = forms.CharField(label='Nome de usuário',
                               strip=True,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Ex: jose.silva',
                                                             'class': 'form-control',
                                                             'autocomplete': 'off'}))

    email = forms.EmailField(label='Email',
                             required=True,
                             widget=forms.EmailInput(attrs={'placeholder': 'jose@gmail.com',
                                                            'class': 'form-control',
                                                            'autocomplete': 'off'}))

    password = forms.CharField(label='Senha',
                               strip=True,
                               required=True,
                               min_length=8,
                               widget=forms.PasswordInput(attrs={'placeholder': '*********',
                                                              'class': 'form-control',
                                                              'autocomplete': 'off'}))

    senha2 = forms.CharField(label='Confirme a senha',
                             strip=True,
                             required=True,
                             min_length=8,
                             widget=forms.PasswordInput(attrs={'placeholder': '*********',
                                                               'class': 'form-control',
                                                               'autocomplete': 'off'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password', 'senha2']

    lista_caracteres = [',', '.', '@', '#', '?', '!', '$', '%', '/', '|', '[', ']',
                        '{', '}', "'", '"', '(', ')', '¬', '*', '<', '>']

    def clean_first_name(self):
        nome = self.cleaned_data.get('first_name')
        for i in nome:
            if i in self.lista_caracteres:
                raise ValidationError(f'O caractere {i} é inválido.')
        return nome

    def clean_last_name(self):
        sobrenome = self.cleaned_data.get('last_name')
        for i in sobrenome:
            if i in self.lista_caracteres:
                raise ValidationError(f'O caractere {i} é inválido.')
        return sobrenome

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Email já cadastrado')

    def clean_password(self):
        password = self.cleaned_data.get('password')
        senha2 = self.cleaned_data.get('senha2')
        if password != senha2:
            raise ValidationError(f'As senhas são diferentes')

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
