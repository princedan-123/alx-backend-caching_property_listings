from django.apps import AppConfig


class PropertiesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'properties'

    def ready(self):
        from .signals import delete_cache_on_delete
        from .signals import delete_cache_on_save
