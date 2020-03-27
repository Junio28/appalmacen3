from django.contrib import admin
from apps.sales.models import Sale,SaleProduct
# Register your models here.

class SaleAdmin(admin.ModelAdmin):
    list_display = ('date','discount','subtotal','total','client')
    ordering = ('date','client')
    search_fields = ('client',)
    list_filter = ('date',)

class SaleProductAdmin(admin.ModelAdmin):
    list_display = ('product','sale','date_sale','price','quantity')
    ordering =('product','date_sale')
    search_fields = ('product','date_sale')
    list_filter = ('product','date_sale')



admin.site.register(Sale,SaleAdmin)
admin.site.register(SaleProduct,SaleProductAdmin)
