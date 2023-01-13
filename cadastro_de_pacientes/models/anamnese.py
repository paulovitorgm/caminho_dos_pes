from django.db import models

class Anamnese(models.Model):
    escolha = [ ('N' , 'Não'),('S' , 'Sim')]
    acompanhamento_medico = models.CharField(max_length= 3, choices= escolha, default=1)
    especialidade = models.CharField(max_length=100, blank=True)
    uso_medicacao = models.CharField(max_length=3, choices= escolha, default=1)
    medicamento_em_uso = models.CharField(max_length=200, blank=True)
    diabetico = models.CharField(max_length=3, choices= escolha, default=1)
    hepatite = models.CharField(max_length=3, choices= escolha, default=1)
    hiv = models.CharField(max_length=3, choices= escolha, default=1)
    problemas_circulatorios = models.CharField(max_length=3, choices= escolha, default=1)
    alergico = models.CharField(max_length=3, choices= escolha, default=1)
    alergia_a = models.CharField(max_length=100, blank=True)
    teve_cancer = models.CharField(max_length=3, choices= escolha, default=1)
    tipo_cancer = models.CharField(max_length=50, blank=True)
    gravidez = models.CharField(max_length=3, choices= escolha, default=1)
    lactante = models.CharField(max_length=3, choices= escolha, default=1)
    hipertensao = models.CharField(max_length=3, choices= escolha, default=1)
    hipotensao = models.CharField(max_length=3, choices= escolha, default=1)
    observacoes = models.TextField(max_length=400, blank=True)
   
       
    