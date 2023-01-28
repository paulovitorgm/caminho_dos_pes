from django.db import models

class Registrar_fornecedor(models.Model):
    cnpj = models.CharField(max_length=14)
    razao_social = models.CharField(max_length=150)
    nome_fantasia = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)