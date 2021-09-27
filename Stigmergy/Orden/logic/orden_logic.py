
# TODO Recuperar el objeto

from ..models import Orden

# TODO Metodos Recuperar Todos

def get_ordenes():
    return Orden.objects.all().order_by('pk')[:10]

# TODO Crear

def create_orden(form):
    orden = form.save()
    orden.save()
    return ()

# TODO Obtener una sola orden

def get_orden_pk(n):
    return Orden.objects.get(pk = n)

# TODO Eliminar una sola orden

def delete_orden_pk(n):
    Orden.objects.filter(pk = n).delete()

# TODO Cambiar el precio

def change_value_orden_pk(n):
    orden = Orden.objects.get(pk = n)
    orden.status = 'Alistamiento'
    orden.save()