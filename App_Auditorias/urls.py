
from django.urls import path

from App_Auditorias.views import*

urlpatterns = [
    path('inicio', inicio, name = "inicio"),
    path('servicios', servicios, name = "servicios"),
    path('nosotros', nosotros, name = "nosotros"),
    path('clientes', clientes, name = "clientes"),
    path('contactanos', contactanos, name = "contactanos"),
    path('eliminarClientes/<id>', eliminarClientes, name = 'eliminarClientes')
    
]
