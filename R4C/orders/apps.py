from django.apps import AppConfig


class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders'

    # Переопределяем метод ready в конфиге приложения, чтобы оно видело наши сигналы
    def ready(self):
        from . import signals
