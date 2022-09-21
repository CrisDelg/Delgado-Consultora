from django.db import models

# Create your models here.

class clientes(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    contacto = models.CharField(max_length=50)
    telefono = models.IntegerField()
    email = models.EmailField()


class servicios(models.Model):
    nombre = models.CharField(max_length=50)