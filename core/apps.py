from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    verbose_name = "Aplicações Principais"

    def ready(self):
        # Implicitly connect signal handlers decorated with @receiver.
        from . import signals
