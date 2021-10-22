from django.contrib import admin

# TODO Referencias 

from . models import Producto, Item, Pedido

# TODO Registrar aplicacion al admin

admin.site.register(Producto)
admin.site.register(Item)
admin.site.register(Pedido)

