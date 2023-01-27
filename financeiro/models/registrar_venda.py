from django.db import models


class Registrar_venda(models.Model):
    data = models.DateField()
    paciente = models.CharField(max_length= 120)
    servico = models.CharField(max_length=200)
    produtos = models.CharField(max_length=120)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    pagamento = models.CharField(max_length=4)
