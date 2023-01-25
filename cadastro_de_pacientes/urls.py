from django.urls import path
from . import views

urlpatterns = [
    path('', views.index ,name='index'),
    path('criar_usuario', views.criar_usuario ,name='criar_usuario'),
    path('cadastrar/paciente', views.cadastro_de_pacientes ,name='cadastro'),
    path('salvar/anamnese/<int:anamnese_id>', views.salvar_anamnese ,name='salvar_anamnese'),
    path('anamnese/<int:paciente_id>', views.anamnese ,name='anamnese'),
    path('busca', views.busca ,name='busca'),
    path('login', views.fazer_login ,name='login'),
    path('logout', views.fazer_logout ,name='logout'),

    ]