from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/paciente', views.cadastro_de_pacientes ,name='cadastro'),
    path('anamnese', views.anamnese ,name='anamnese'),
]