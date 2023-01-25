from django.db import models
from .cadastro_pacientes import Cadastro_de_paciente


class Anamnese(models.Model):
    """paciente, acompanhamento_medico, especialidade, uso_medicacao, medicamento_em_uso, diabetico, hepatite, hiv, problemas_circulatorios, alergico, alergia_a, teve_cancer, tipo_cancer,gravidez, lactante, hipertensao, hipotensao"""
    paciente = models.ForeignKey(Cadastro_de_paciente, on_delete=models.CASCADE, related_name='anamneses')
    escolha = [ ('N' , 'Não'),('S' , 'Sim')]
    acompanhamento_medico = models.CharField(max_length= 3, choices= escolha)
    especialidade = models.CharField(max_length=100, blank=True)
    uso_medicacao = models.CharField(max_length=3, choices= escolha)
    medicamento_em_uso = models.CharField(max_length=200, blank=True)
    diabetico = models.CharField(max_length=3, choices= escolha)
    hepatite = models.CharField(max_length=3, choices= escolha)
    hiv = models.CharField(max_length=3, choices= escolha)
    problemas_circulatorios = models.CharField(max_length=3, choices= escolha)
    alergico = models.CharField(max_length=3, choices= escolha)
    alergia_a = models.CharField(max_length=100, blank=True)
    teve_cancer = models.CharField(max_length=3, choices= escolha)
    tipo_cancer = models.CharField(max_length=50, blank=True)
    gravidez = models.CharField(max_length=3, choices= escolha)
    lactante = models.CharField(max_length=3, choices= escolha)
    hipertensao = models.CharField(max_length=3, choices= escolha)
    hipotensao = models.CharField(max_length=3, choices= escolha)
    observacoes = models.TextField(max_length=400, blank=True)
   
       
    