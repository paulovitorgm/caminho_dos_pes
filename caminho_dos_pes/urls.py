from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pacientes/', include('cadastro_de_pacientes.urls')),
    path('usuarios/',include('usuarios.urls')),
    # path('cadastro_pacientes', include('cadastro_de_pacientes.urls')),
]
