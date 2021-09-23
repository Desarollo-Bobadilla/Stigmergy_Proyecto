from django.db import models

# TODO Referencias externas

from Producto.models import Producto

# TODO Modelo del proyecto

class Item (models.Model):

    # TODO Primary key
    
    id = models.AutoField(primary_key=True)

    # TODO Atributos

    cantidad = models.IntegerField()

    # TODO Relaciones

    produc = models.OneToOneField(Producto, on_delete=models.CASCADE)

    # TODO String representation of any object

    def __str__(self):
        return '%s' % (self.cantidad)
