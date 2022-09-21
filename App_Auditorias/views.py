from mailbox import NoSuchMailboxError
from django.shortcuts import render

from .models import*
from App_Auditorias.forms import contactanos

# Create your views here.

def inicio(request):
    return render (request, "App_Auditorias/principal.html")

def servicios(request):
    return render (request, "App_Auditorias/servicios.html")

def nosotros(request):
    return render(request, "App_Auditorias/nosotros.html")

def clientes(request):
    return render (request, "App_Auditorias/inicio.html")


'''def clientes(request):
    if request.method == "POST":
        form = clientes(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre = info['nombre']
            categoria = info['categoria']
            cliente = clientes(nombre=nombre, categoria=categoria)
            cliente.save()
            cliente = clientes.objects.all()
            return render(request, "App_Auditorias/clientes.html", {'cliente':cliente})
    else:
        form=clientes()
        return render(request, "App_Auditorias/clientes.html", {'formulario':form})'''    
    

def contactanos(request):
    '''if request.method == 'POST':
        nombre = request.POST['nombre']
        telefono = request.POST['telefono']
        email = request.POST['email']
        contacto = contactanos(nombre='nombre', telefono='telefono', email='email')
        contacto.save()
        return render (request, "App_Auditorias/contactanos.html")'''


    return render (request, "App_Auditorias/contactanos.html")

def eliminarClientes(request, id):
    cliente =clientes.object.get(id=id)
    cliente.delete()
    cliente = clientes.objects.all()
    return render (request, "App_Auditorias/clientes.html", {'cliente':cliente})