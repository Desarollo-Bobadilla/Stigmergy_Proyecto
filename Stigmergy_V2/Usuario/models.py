from django.db import models


# TODO Modelo del proyecto (Padre)

class Usuario (models.Model):

    # TODO Primary key
    
    id = models.AutoField(primary_key=True)

    # TODO Atributos

    nombre = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)

    # TODO Herencia

    class Meta:
        abstract = True




# TODO Modelo del proyecto (Hijo)

class Comprador (Usuario):

    # TODO Atributos

    preferencias = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)

    # TODO String representation of any object

    def __str__(self):
        return '%s' % (self.nombre)
