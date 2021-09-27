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

    CREADA = 'Creada'
    ALISTAMIENTO = 'Alistamiento'
    LISTA = 'Lista'
    EN_HUB_DESPACHO = 'En Hub Despacho'
    VOLANDO = 'Volando'
    EN_HUB_LLEGADA = 'En Hub Llegada'
    LISTA_RECOGER = 'Lista Recoger'
    ENTREGADA = 'Entregada'
    CANCELADA = 'Cancelada'

    CHOICES = (
        (CREADA, 'Creada'),
        (ALISTAMIENTO, 'Alistamiento'),
        (LISTA, 'Lista'),
        (EN_HUB_DESPACHO, 'En Hub Despacho'),
        (VOLANDO, 'Volando'),
        (EN_HUB_LLEGADA, 'En Hub Llegada'),
        (LISTA_RECOGER, 'Lista Recoger'),
        (ENTREGADA, 'Entregada'),
        (CANCELADA, 'Cancelada')
    )

    status = models.CharField(max_length=255, choices=CHOICES, default=CREADA)

    # TODO Relaciones
    
    comprador = models.ForeignKey(Comprador, on_delete=models.CASCADE, default=None)
    items = models.ManyToManyField(Item)

    # TODO Atributos de simbolismo a las relaciones de los Hubs

    hubEntrega = models.IntegerField(null=True)
    hubRecepcion = models.IntegerField(null=True)

    # TODO String representation of any object

    def __str__(self):
        return '%s %s' % (self.identificate, self.precioTotal)
