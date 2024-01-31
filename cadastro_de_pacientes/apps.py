from django.apps import AppConfig


class CadastroDePacientesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cadastro_de_pacientes'

    def ready(self):
        from cadastro_de_pacientes import signals