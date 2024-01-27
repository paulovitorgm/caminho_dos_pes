from django.contrib.auth.models import User
from django.db import models


class Usuario(models.Model):
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
