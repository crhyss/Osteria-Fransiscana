
from datetime import datetime
from importlib.metadata import requires
from tkinter import Widget
from django import forms
from .models import Usuario, Direccion, Region, Reclamo
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
import datetime
def agregarClaseFormControl(elementos):
    for campo in elementos:
        campo.field.widget.attrs['class'] = 'form-control'

class inicioForm(UserCreationForm):
    pass

class userForm(forms.ModelForm):

    class Meta:
        model = Usuario

        fields = ['usr_nombre','usr_apellido_pat','usr_apellido_mat', 'usr_correo', 'usr_pass']
        labels = {
            'usr_nombre':'Nombre',
            'usr_apellido_pat':'Apellido Paterno',
            'usr_apellido_mat':'Apellido Materno',
            'usr_correo':'Correo',
            'usr_pass':'Contraseña',
            'pass_confirm':'Confirme su contraseña',
        }
        
        widgets = {
            'usr_pass': forms.PasswordInput(),
        }

class direccionForm(ModelForm):
    class Meta:
        model = Direccion
        fields = ['dir_calle', 'dir_nro', 'dir_depto_nro', 'dir_comuna']
        requires = {
            'dir_depto_nro' : forms.IntegerField(required=False)
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
        

    

