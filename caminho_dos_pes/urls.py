from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pacientes/', include('cadastro_de_pacientes.urls')),
    path('', include('usuarios.urls')),
    path('financeiro/', include('financeiro.urls')),
    # path('cadastro_pacientes', include('cadastro_de_pacientes.urls')),
]
