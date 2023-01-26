from django.urls import path
from . import views

urlpatterns = [
    path('registrar/procedimento', views.registar_procedimento, name='registar_procedimento'),
]