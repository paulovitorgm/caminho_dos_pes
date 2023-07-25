from .models import Usuario
from django import forms


class Formulario_usuario(forms.ModelForm):
    nome = forms.CharField(label='Nome', required=True, widget=forms.TextInput(attrs={'placeholder':'Ex: José', 'class':'form-control', 'autocomlete': 'off'}))
    sobrenome = forms.CharField(label='Sobrenome', required=True, widget=forms.TextInput(attrs={'placeholder':'Ex: da Silva', 'class':'form-control', 'autocomlete': 'off'}))  
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(attrs={'placeholder':'jose@gmail.com', 'class':'form-control', 'autocomlete': 'off'}))   
    senha = forms.CharField(label='Senha', required=True, widget=forms.PasswordInput(attrs={'placeholder':'*********', 'class':'form-control', 'autocomlete': 'off'}))  
    senha2 = forms.CharField(label='Confirme a senha', required=True, widget=forms.PasswordInput(attrs={'placeholder':'*********', 'class':'form-control', 'autocomlete': 'off'}))

    class Meta:
        model = Usuario
        exclude = ['']