
# TODO Recuperar el objeto

from ..models import Pedido

# TODO Metodos Recuperar Todos

def get_ordenes():
    return Pedido.objects.all().order_by('pk')[:10]

# TODO Crear

def create_orden(form):
    orden = form.save()
    orden.save()
    return ()

# TODO Obtener una sola orden

def get_orden_pk(n):
    return Pedido.objects.get(pk = n)

# TODO Eliminar una sola orden

def delete_orden_pk(n):
    Pedido.objects.filter(pk = n).delete()

# TODO Cambiar el precio

def change_value_orden_pk(n):
    orden = Pedido.objects.get(pk = n)
    orden.status = 'Alistamiento'
    orden.save()