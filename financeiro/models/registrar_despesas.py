from django.db import models



class Registrar_despesa(models.Model):
    fornecedor = models.CharField(max_length=100)
    data = models.DateField()
    produtos = models.CharField(max_length=300)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    pagamento = models.CharField(max_length=4)
    observacoes = models.CharField(max_length=300)