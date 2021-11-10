from django.shortcuts import render

# TODO Recuper los metodos de la lógica

from .logic.pedido_logic import *
from .forms import PedidoForm

from django.http import HttpResponse
from django.core import serializers
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

# TODO AUTH0

from django.contrib.auth.decorators import login_required
from Stigmergy.auth0backend import getRole

# ----------------------------------------------------------------------------------

# TODO Recuperar Todas

@login_required
def get_all_ordenes(request):

    role = getRole(request)
    if role != "Big Boss":
        return HttpResponse("Unauthorized User")

    if request.method == 'GET':

        context = {
            'ordenes_list': get_ordenes()
        }
        return render(request, 'Orden/ordenes.html', context)

@login_required
def get_orden(request, pk):

    role = getRole(request)
    if role != "Big Boss":
        return HttpResponse("Unauthorized User")

    if request.method == 'GET':
        orden = serializers.serialize('json', [get_orden_pk(pk)])
        return HttpResponse(orden, content_type = 'application/json')

@login_required
def delete_orden(request, pk):

    role = getRole(request)
    if role != "Big Boss":
        return HttpResponse("Unauthorized User")

    if request.method in ['GET', 'DELETE']:
        delete_orden_pk(pk)

        ordenes_list = serializers.serialize('json', get_ordenes())
        return HttpResponse(ordenes_list, content_type = 'application/json')

@login_required
def change_orden(request, pk):

    role = getRole(request)
    if role != "Big Boss":
        return HttpResponse("Unauthorized User")

    if request.method in ['PUT', 'GET']: # REVISAR, DEBERÍA SER put

        change_value_orden_pk(pk)

        context = {
            'ordenes_list': get_ordenes()
        }

        return render(request, 'Orden/ordenChange.html', context)

# ----------------------------------------------------------------------------------

# TODO Crear

@login_required
def orden_create(request):

    role = getRole(request)
    if role != "Big Boss" or role != "User":
        return HttpResponse("Unauthorized User")

    if request.method == 'POST':

        form = PedidoForm(request.POST)

        #print('\n', form.data, '\n')

        if form.is_valid():

            create_orden(form)
            messages.add_message(request, messages.SUCCESS, 'Orden create successful')
            return HttpResponseRedirect(reverse('Orden_Create'))
            
        else:
            print('\n', form.errors, '\n')
    else:
        form = PedidoForm()

    context = {
        'form': form,
    }

    return render(request, 'Orden/ordenCreate.html', context)