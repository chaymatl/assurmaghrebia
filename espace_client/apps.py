from django.apps import AppConfig

class EspaceClientConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'espace_client'

    def ready(self):
        import espace_client.signals