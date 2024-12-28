# bind/apps.py
from django.apps import AppConfig


class BindConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bind'

    def ready(self):
        import bind.signals  # Импортируем сигналы
