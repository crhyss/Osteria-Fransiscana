
from importlib.metadata import requires
from tkinter import Widget
from django import forms
from .models import Usuario, Direccion, Region
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

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


    

