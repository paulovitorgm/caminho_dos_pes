from django.db import models
from .registrar_fornecedores import Registrar_fornecedor


class Registrar_despesa(models.Model):
    fornecedor = models.ForeignKey(Registrar_fornecedor, on_delete=models.CASCADE)
    data = models.DateField()
    produtos = models.CharField(max_length=300)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    meios_de_pagamento = [('cred','Crédito'),('deb','Débito'),('pix','Pix'), ('din', 'Dinheiro')]
    pagamento = models.CharField(max_length=4, choices=meios_de_pagamento)