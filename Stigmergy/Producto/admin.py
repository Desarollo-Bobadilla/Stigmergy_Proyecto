from Producto.models import Producto
from django.contrib import admin

# TODO Referencias 

from . models import Producto

# TODO Registrar aplicacion al admin

admin.site.register(Producto)
