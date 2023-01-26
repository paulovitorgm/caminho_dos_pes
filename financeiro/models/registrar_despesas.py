from django.db import models
from datetime import datetime
from django.contrib.auth.models import 


class Registrar_venda(models.Model):
    data = models.DateField(label='Data da pesquisa',disabled=True, initial=datetime.today)
    # comprador = models.ForeignKey()
    # autorizacao = 
    total = models.DecimalField(max_digits=10, decimal_places=2)
    meios_de_pagamento = [('cred','Crédito'),('deb','Débito'),('pix','Pix'), ('din', 'Dinheiro')]
    pagamento = models.CharField(max_length=4, choices=meios_de_pagamento)