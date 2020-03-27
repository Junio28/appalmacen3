from django.apps import AppConfig


class SalesConfig(AppConfig):
    name = 'apps.sales'
    verbose_name="Gestor de Ventas"


class SaleProductConfig(AppConfig):
    name = 'apps.sales'
    verbose_name="Gestor de Ventas por Productos"
    
