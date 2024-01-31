from django.db.models.signals import post_save
from django.dispatch import receiver

from cadastro_de_pacientes.models import Anamnese
from cadastro_de_pacientes.models.cadastro_pacientes import CadastroDePaciente


@receiver(post_save, sender=CadastroDePaciente)
def cria_anamnese(sender, created, instance, **kwargs):
    if created or not hasattr(instance, "anamnese"):
        Anamnese.objects.create(paciente=instance)
