from django.urls import path
from usuarios.views import *

urlpatterns = [
    path('criar_usuario', criar_usuario, name='criar_usuario'),
    path('editar_usuario', editar_usuario, name='editar_usuario'),
    path('login', fazer_login, name='login'),
    path('logout', fazer_logout, name='logout'),
    ]
