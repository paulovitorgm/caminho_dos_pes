from django.urls import path
from . import views

urlpatterns = [
    path('registrar/procedimento', views.registar_procedimento, name='registrar_procedimento'),
    path('registrar/venda', views.registrar_venda, name='registrar_venda'),
    path('registrar/despesa', views.registrar_despesa, name='registrar_despesa'),
    
]