from django.apps import AppConfig


class FgphConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "FGPH"

    #override
    def ready(self):
        import FGPH.signals