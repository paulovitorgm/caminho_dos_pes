from django.db import models
from .cadastro_pacientes import Cadastro_de_paciente

escolha = [('N', 'Não'), ('S', 'Sim')]


class Anamnese(models.Model):
    """paciente, acompanhamento_medico, especialidade, uso_medicacao, medicamento_em_uso,
       diabetico, hepatite, hiv, problemas_circulatorios, alergico, alergia_a, teve_cancer,
       tipo_cancer,gravidez, lactante, hipertensao, hipotensao"""
    paciente = models.ForeignKey(Cadastro_de_paciente, on_delete=models.CASCADE, related_name='anamneses')
    acompanhamento_medico = models.CharField(max_length=1, choices=escolha, default='N')
    especialidade = models.CharField(max_length=100, blank=True)
    uso_medicacao = models.CharField(max_length=1, choices=escolha, default='N')
    medicamento_em_uso = models.CharField(max_length=200, blank=True)
    diabetico = models.CharField(max_length=1, choices=escolha, default='N')
    hepatite = models.CharField(max_length=1, choices=escolha, default='N')
    hiv = models.CharField(max_length=1, choices=escolha, default='N')
    problemas_circulatorios = models.CharField(max_length=1, choices=escolha, default='N')
    alergico = models.CharField(max_length=1, choices=escolha, default='N')
    alergia_a = models.CharField(max_length=100, blank=True)
    teve_cancer = models.CharField(max_length=1, choices=escolha, default='N')
    tipo_cancer = models.CharField(max_length=50, blank=True)
    gravidez = models.CharField(max_length=1, choices=escolha, default='N')
    lactante = models.CharField(max_length=1, choices=escolha, default='N')
    hipertensao = models.CharField(max_length=1, choices=escolha, default='N')
    hipotensao = models.CharField(max_length=1, choices=escolha, default='N')
    observacoes = models.TextField(max_length=400, blank=True)
   
       
    