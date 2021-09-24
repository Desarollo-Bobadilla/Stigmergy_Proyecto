from django.shortcuts import render

# TODO Recuper los metodos de la lógica

from .logic.orden_logic import *
from .forms import OrdenForm

from django.http import HttpResponse
from django.core import serializers
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

# ----------------------------------------------------------------------------------

# TODO Recuperar Todas

def get_all_ordenes(request):

    if request.method == 'GET':
        ordenes_list = serializers.serialize('json', get_ordenes())
        return HttpResponse(ordenes_list, content_type = 'application/json')


def get_orden(request, pk):

    if request.method == 'GET':
        orden = serializers.serialize('json', [get_orden_pk(pk)])
        return HttpResponse(orden, content_type = 'application/json')

def delete_orden(request, pk):

    if request.method == 'GET': # REVISAR, DEBERÍA SER DELETE
        delete_orden_pk(pk)

        ordenes_list = serializers.serialize('json', get_ordenes())
        return HttpResponse(ordenes_list, content_type = 'application/json')

def change_orden(request, pk):

    if request.method == 'GET': # REVISAR, DEBERÍA SER put

        change_value_orden_pk(pk)

        orden = serializers.serialize('json', [get_orden_pk(pk)])
        return HttpResponse(orden, content_type = 'application/json')

# ----------------------------------------------------------------------------------

# TODO Crear

def orden_create(request):

    if request.method == 'POST':

        form = OrdenForm(request.POST)

        if form.is_valid():

            create_orden(form)
            messages.add_message(request, messages.SUCCESS, 'Orden create successful')
            return HttpResponseRedirect(reverse('orden_create'))
            
        else:
            print(form.errors)
    else:
        form = OrdenForm()