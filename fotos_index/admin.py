from django.contrib import admin
from fotos_index.models import Fotos as model_Fotos
# Register your models here.

class Fotos(admin.ModelAdmin):
    list_display = ["id","titulo"]
    list_display_links = ["id","titulo"]
    search_fields = ['titulo']
    list_per_page = 10

admin.site.register(model_Fotos, Fotos)
