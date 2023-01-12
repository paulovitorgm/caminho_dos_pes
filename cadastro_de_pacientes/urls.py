from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastro_de_pacientes ,name='cadastro'),
]