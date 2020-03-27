from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.

from apps.products.models import Product
from apps.clients.models import Client

class Sale(models.Model):
    date = models.DateField(default=now, verbose_name="Fecha")
    discount= models.DecimalField(max_digits=8, decimal_places=2,verbose_name=" Descuento")
    subtotal= models.DecimalField(max_digits=8, decimal_places=2,verbose_name=" Subtotal")
    total= models.DecimalField(max_digits=8, decimal_places=2,verbose_name=" Total")
    client =models.ForeignKey(Client,
                                    null=True,
                                    blank=True,
                                    on_delete=models.CASCADE)
    
    user=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    product=models.ManyToManyField(Product, through='SaleProduct', verbose_name="Producto")
    created=models.DateField(auto_now=True, verbose_name="Fecha de creacion")
    updated=models.DateField(auto_now=True, verbose_name="Fecha de edicion")

    class Meta:
        verbose_name="Venta"
        verbose_name_plural="Ventas"

    

class SaleProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Producto")
    sale=models.ForeignKey(Sale, on_delete=models.CASCADE, verbose_name="Venta")
    date_sale=models.DateTimeField(auto_now=True,verbose_name="Fecha")
    price=models.IntegerField(verbose_name="Precio")
    quantity=models.IntegerField(verbose_name="Cantidad")

    #def __str__(self):
     #   return self.product

    class Meta:
        verbose_name="Ventaxproduct"
        verbose_name_plural="Ventaxproductos"