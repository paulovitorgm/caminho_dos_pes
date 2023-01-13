from django.db import models

class Cadastro_de_paciente(models.Model):
    nome_paciente = models.CharField(max_length=200)
    sobrenome_paciente = models.CharField(max_length=200)
    telefone = models.CharField(max_length=11)
    primeiro_atendimento = models.DateField()
    email = models.EmailField(max_length=200)
    nome_completo = nome_paciente, sobrenome_paciente
    sexo =[
        ('M' , 'Masculino'),
        ('F' , 'Feminino'),
        ]
    sexo_sexo = models.CharField(max_length = 1, choices = sexo, default=0) 
    foto = models.FileField()
