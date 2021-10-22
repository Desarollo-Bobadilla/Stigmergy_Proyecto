
# TODO Formato que se envia desde JMeter para las pruebas

from django import forms
from .models import Pedido

class PedidoForm(forms.ModelForm):

    class Meta:
        
        model = Pedido
        fields = [
            'identificate',
            'precioTotal',
            'comprador',
            'items',
            'hubEntrega',
            'hubRecepcion',
            'status'
        ]

        labels = {
            'identificate' : 'Identificate',
            'precioTotal' : 'PrecioTotal',
            'comprador' : 'Comprador',
            'items' : 'Items',
            'hubEntrega' : 'HubEntrega',
            'hubRecepcion' : 'HubRecepcion',
            'status' : 'Status'
        }