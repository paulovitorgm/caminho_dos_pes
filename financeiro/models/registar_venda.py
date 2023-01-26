from django.db import models
from datetime import datetime
from ...cadastro_de_pacientes.models.cadastro_pacientes import Cadastro_de_paciente


class Registrar_venda(models.Model):
    data = models.DateField(label='Data da pesquisa', initial=datetime.today)
    paciente = models.ForeignKey(Cadastro_de_paciente,on_delete=models.CASCADE)
    servico = models.CharField(max_length=200)
    produto = models.CharField(max_length=120)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    meios_de_pagamento = [('cred','Crédito'),('deb','Débito'),('pix','Pix'), ('din', 'Dinheiro')]
    pagamento = models.CharField(max_length=4, choices=meios_de_pagamento)
