from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/paciente', views.cadastro_de_pacientes ,name='cadastro'),
    path('salvar/anamnese/<int:anamnese_id>', views.salvar_anamnese ,name='salvar_anamnese'),
    path('anamnese/<int:paciente_id>', views.anamnese ,name='anamnese'),
    path('busca', views.busca ,name='busca'),
    ]