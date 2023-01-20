from django.urls import path
from . import views

urlpatterns = [
    path('', views.index ,name='index'),
    path('criar_usuario', views.criar_usuario ,name='criar_usuario'),
    path('cadastrar/paciente', views.cadastro_de_pacientes ,name='cadastro'),
    path('anamnese/preencher', views.preencher_anamnese ,name='preencher_anamnese'),
    path('anamnese', views.ver_anamnese ,name='ver_anamnese'),
    path('busca', views.busca ,name='busca'),
    path('login', views.fazer_login ,name='login'),
    path('logout', views.fazer_logout ,name='logout'),

    ]