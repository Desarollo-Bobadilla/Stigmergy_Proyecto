from django.db import models

# TODO Referencias externas

from Usuario.models import Comprador
from Item.models import Item

# TODO Modelo del proyecto

class Orden (models.Model):

    # TODO Primary key
    
    id = models.AutoField(primary_key=True)

    # TODO Atributos

    identificate = models.IntegerField()
    precioTotal = models.FloatField(null=True, blank=True, default=None)

    # TODO Relaciones
    
    comprador = models.ForeignKey(Comprador, on_delete=models.CASCADE, default=None)
    items = models.ManyToManyField(Item)

    #hubEntrega
    #hubRecepción =

    # TODO String representation of any object

    def __str__(self):
        return '%s %s' % (self.identificate, self.precioTotal)
