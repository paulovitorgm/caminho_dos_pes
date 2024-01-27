from django.contrib import admin
from financeiro.formularios import RegistrarVenda
from financeiro.formularios import RegistrarDespesa



# Register your models here.

class Registro_de_venda(admin.ModelAdmin):
    list_display = ['paciente', 'servico', 'produtos', 'data']
    list_display_links = ['paciente', 'servico']
    list_filter = [ 'data', 'servico', 'produtos']
    list_per_page = 20


class Registro_de_despesa(admin.ModelAdmin):
    list_display = ['fornecedor','produtos', 'data', 'pagamento']
    list_display_links = ['fornecedor','produtos']
    list_filter = ['data', 'fornecedor']
    list_per_page = 20
    search_fields = ["produtos", "fornecedor", "pagamento"]

admin.site.register(RegistrarVenda, Registro_de_venda)
admin.site.register(RegistrarDespesa, Registro_de_despesa)