
from datetime import datetime
from importlib.metadata import requires
from tkinter import Widget
from django import forms
from .models import User, Direccion, Region, Reclamo, Reserva
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
import datetime
def agregarClaseFormControl(elementos):
    for campo in elementos:
        campo.field.widget.attrs['class'] = 'form-control'

class inicioForm(UserCreationForm):
    pass

class profileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(profileForm,self).__init__(*args, **kwargs)
        agregarClaseFormControl(self.visible_fields())
    class Meta:
        model = User
        fields = ['user_nombre', 'user_apellidos',
                  'password', 'user_correo']

        labels = {
            'user_nombre' : 'Nombre',
            'user_apellidos' : 'Apellidos',
            'password' : 'Contraseña',
            'user_correo' : 'Correo',
        }

class userForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['user_nombre','user_apellidos', 'user_correo']
        labels = {
            'user_nombre':'Ingrese sus nombres',
            'user_apellidos':'Ingrese sus apellidos',
            'user_correo':'Ingrese su correo',
        }

class direccionForm(ModelForm):
    class Meta:
        model = Direccion
        fields = ['dir_calle', 'dir_nro', 'dir_depto_nro']

        labels = {
            'dir_calle': 'Ingrese el nombre de la calle',
            'dir_nro': 'Ingrese el número de la casa',
            'dir_depto_nro': 'Ingrese el número del departamento'
        }

        widgets = {
            'dir_nro': forms.NumberInput(),
            'dir_depto_nro': forms.NumberInput(),
        }

class reclamoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(reclamoForm,self).__init__(*args, **kwargs)
        agregarClaseFormControl(self.visible_fields())
        self.fields['reclamo_fecha'].widget.attrs['disabled'] = 'disabled' 
        self.fields['reclamo_fecha'].widget.format = '%d/%m/%Y %H:%M'
    class Meta:
        model = Reclamo
        fields = ['nombre','apellido','reclamo_fecha', 'reclamo_descrip']
        widgets = {
            
            'reclamo_fecha': forms.DateTimeInput(attrs={'class': 'form-control'}),
            
        }
        
class reservaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(reservaForm,self).__init__(*args, **kwargs)
        agregarClaseFormControl(self.visible_fields())
    class Meta:
        model = Reserva
        fields = ['id_reserva', 'fecha_reserva', 'reserva_usuario', 'reserva_mesa']
        labels = {
            'id_reserva': 'ID' ,
            'fecha_reserva' : 'Reserva',
            'reserva_usuario' : 'Usuario',
            'reserva_mesa' : 'Mesa'
        }


