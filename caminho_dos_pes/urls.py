from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cadastro_de_pacientes.urls')),
    # path('cadastro_pacientes', include('cadastro_de_pacientes.urls')),
]
