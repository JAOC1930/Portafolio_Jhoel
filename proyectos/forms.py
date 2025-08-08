from django import forms
from proyectos.models import *

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'email', 'celular', 'mensaje']
