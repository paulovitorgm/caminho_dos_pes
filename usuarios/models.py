from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField(max_length=160)
    senha = models.CharField(max_length=36)