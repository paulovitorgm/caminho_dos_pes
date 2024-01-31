from django.contrib import admin
from cadastro_de_pacientes.models.cadastro_pacientes import CadastroDePaciente


# Register your models here.

class CadastroDePacienteAdmin(admin.ModelAdmin):
    list_display = ["id", "nome_paciente", "telefone"]
    list_display_links = ["id", "nome_paciente"]
    list_per_page = 10
    search_fields = ["nome_paciente"]


admin.site.register(CadastroDePaciente, CadastroDePacienteAdmin)
