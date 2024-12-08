from django.apps import AppConfig

class DatabaseDatasource(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shop.db'