
# TODO Recuperar la conexión con la vista

from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

# TODO Rutas personales

urlpatterns = [

    path('list/', views.get_all_ordenes, name='ordenes_list'),
    path('see/<int:pk>/', views.get_orden, name='get_orden_by_pk'),
    path('delete/<int:pk>/', views.delete_orden, name='delete_orden_by_pk'),

    path('change/<int:pk>/', csrf_exempt(views.change_orden), name='change_ordent_by_pk'),
    path('orden_create/', csrf_exempt(views.orden_create), name='Orden_Create')
]