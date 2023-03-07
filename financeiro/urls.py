from django.urls import path
from . import views

urlpatterns = [
    path('registrar/procedimento', views.registar_procedimento, name='registrar_procedimento'),
    path('registrar/despesa', views.registrar_despesa, name='registrar_despesa'),
    path('entradas', views.entradas, name='entradas'),
    path('saidas', views.saidas, name='saidas'),
    
]