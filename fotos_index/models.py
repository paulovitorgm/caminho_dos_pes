from django.db import models


class Fotos(models.Model):
    foto = models.ImageField(upload_to="fotos_procedimento", blank=True)
    titulo = models.CharField(max_length=50, blank=True)
    descricao = models.TextField(max_length=200, blank=True)
