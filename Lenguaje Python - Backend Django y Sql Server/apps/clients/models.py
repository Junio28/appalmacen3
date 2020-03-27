from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    lastname = models.CharField(max_length=50, verbose_name="Apellido")
    phone = models.CharField(max_length=50, verbose_name="Telefono")
    address = models.CharField(max_length=50,verbose_name="Direccion")


    def __str__(self):   # para que al momento que se relacione la tabla, en el selector me salgan los nombres de los clientes
        return self.name +" "+ self.lastname +" "

    class meta:
        verbose_name="cliente"
        verbose_name_plural="Clientes"

