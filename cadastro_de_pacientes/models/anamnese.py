from django.db import models
from cadastro_de_pacientes.models import CadastroDePaciente
from apps.materiais_em_comum import escolha


class Anamnese(models.Model):
    """paciente, acompanhamento_medico, medicamento_em_uso, diabetico, hepatite, hiv,
       alergico, teve_cancer, gravidez, lactante, hipertensao, hipotensao"""
    paciente = models.OneToOneField(CadastroDePaciente,
                                 on_delete=models.CASCADE,
                                 related_name='anamnese')

    acompanhamento_medico = models.CharField(max_length=100,
                                     blank=True,
                                     default='Não faz')

    medicamento_em_uso = models.CharField(max_length=200,
                                          blank=True,
                                          default='Não faz')

    diabetico = models.CharField(max_length=50,
                                 choices=escolha,
                                 default='Não')

    hepatite = models.CharField(max_length=1,
                                choices=escolha,
                                default='N')

    hiv = models.CharField(max_length=1,
                           choices=escolha,
                           default='N')

    alergico = models.CharField(max_length=50,
                                default='Nenhuma')

    teve_cancer = models.CharField(max_length=50,
                                   default='Não')

    gravidez = models.CharField(max_length=1,
                                choices=escolha,
                                default='N')

    lactante = models.CharField(max_length=1,
                                choices=escolha,
                                default='N')

    hipertensao = models.CharField(max_length=1,
                                   choices=escolha,
                                   default='N')

    hipotensao = models.CharField(max_length=1,
                                  choices=escolha,
                                  default='N')

    observacoes = models.TextField(max_length=400,
                                   blank=True)
   
       
    