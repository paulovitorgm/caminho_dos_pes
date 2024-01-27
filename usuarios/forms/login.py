from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginForm(forms.ModelForm):
    username = forms.CharField(label='Nome de usuário',
                               strip=True,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Ex: jose.silva',
                                                             'class': 'form-control',
                                                             'autocomplete': 'off'}))

    password = forms.CharField(label='Senha',
                               strip=True,
                               required=True,
                               min_length=8,
                               widget=forms.PasswordInput(attrs={'placeholder': '*********',
                                                                 'class': 'form-control',
                                                                 'autocomplete': 'off'}))

    class Meta:
        model = User
        fields = ['username', 'password']
