from django.urls import path
from cadastro_de_pacientes.views import *

urlpatterns = [
    path('cadastrar/paciente', cadastro_de_pacientes, name='cadastro'),
    path('salvar/anamnese/<int:anamnese_id>', salvar_anamnese, name='salvar_anamnese'),
    path('anamnese/<int:paciente_id>', anamnese, name='anamnese'),
    path('busca/', busca, name='busca'),
    ]

