from .models import Usuario
from django import forms


class Formulario_usuario(forms.ModelForm):
    nome = forms.CharField(label='Nome', widget=forms.TextInput(attrs={'placeholder':'Ex: José'}))
    sobrenome = forms.CharField(label='Sobrenome', widget=forms.TextInput(attrs={'placeholder':'Ex: da Silva'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'placeholder':'jose@gmail.com'}))
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'placeholder':'*********'}))
    senha2 = forms.CharField(label='Confirme a senha', widget=forms.PasswordInput(attrs={'placeholder':'*********'}))

    class Meta:
        model = Usuario
        exclude = ['']