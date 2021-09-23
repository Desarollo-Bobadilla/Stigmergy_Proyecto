from Item.models import Item
from django.contrib import admin

# TODO Referencias 

from . models import Item

# TODO Registrar aplicacion al admin

admin.site.register(Item)
