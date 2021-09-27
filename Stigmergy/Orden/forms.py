
# TODO Formato que se envia desde JMeter para las pruebas

from django import forms
from .models import Orden

class OrdenForm(forms.ModelForm):

    class Meta:
        
        model = Orden
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