from django.db import models

# TODO Modelo del proyecto

class Producto (models.Model):

    # TODO Primary key
    
    id = models.AutoField(primary_key=True)

    # TODO Atributos

    nombre = models.CharField(max_length=50)
    precio = models.FloatField(null=True, blank=True, default=None)
    alto = models.FloatField(null=True, blank=True, default=None)
    ancho = models.FloatField(null=True, blank=True, default=None)
    largo = models.FloatField(null=True, blank=True, default=None)
    peso = models.FloatField(null=True, blank=True, default=None)
    cantidadDisponible = models.IntegerField()

    # TODO String representation of any object

    def __str__(self):
        return '%s %s' % (self.nombre, self.precio)
