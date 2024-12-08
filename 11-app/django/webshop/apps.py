from django.apps import AppConfig
from shop.use_cases.plugin_recognition import PluginService

datasource_group = 'shop.datasource'

class ShopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'webshop'
    plugin_service = PluginService()

    def ready(self):
        # On application start load all plugins
        self.plugin_service.load_plugins(datasource_group)