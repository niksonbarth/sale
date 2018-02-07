from django.apps import AppConfig
from watson import search as watson

class CatalogConfig(AppConfig):
    name = 'catalog'
    verbose_name = 'Catálogo'

    def ready(self):
        Ad = self.get_model('Ad')
        watson.register(Ad)
