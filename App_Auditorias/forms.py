from django import forms


class clientes(forms.Form):
    nombre = forms.CharField(max_length=50)
    categoria = forms.CharField(max_length=50)
    contacto = forms.CharField(max_length=50)
    telefono = forms.IntegerField()
    email = forms.EmailField()

class contactanos(forms.Form):
    nombre = forms.CharField(max_length=50)
    telefono = forms.IntegerField()
    email = forms.EmailField()