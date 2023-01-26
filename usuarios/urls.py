from django.urls import path
from . import views

urlpatterns = [
    path('', views.index ,name='index'),
    path('criar_usuario', views.criar_usuario ,name='criar_usuario'),
    path('login', views.fazer_login ,name='login'),
    path('logout', views.fazer_logout ,name='logout'),
    ]