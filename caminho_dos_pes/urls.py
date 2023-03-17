from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fotos_index.urls')),
    path('pacientes/', include('cadastro_de_pacientes.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('financeiro/', include('financeiro.urls')),
    ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
