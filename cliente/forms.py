
from .models import Usuario, Direccion
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

def agregarClaseFormControl(elementos):
    for campo in elementos:
        campo.field.widget.attrs['class'] = 'form-control'

class inicioForm(UserCreationForm):
    pass

class direccionForm(ModelForm):
    class Meta:
        model = Direccion
        fields = ['codigo_postal']

    

