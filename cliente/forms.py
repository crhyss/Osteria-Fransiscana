
from select import select
from tkinter.tix import Select
from .models import Usuario, Direccion, Comuna,Region
from django.forms import ModelForm,EmailInput,ModelChoiceField,Form,TextInput,Textarea 
from django.contrib import admin
from django import forms
from django.db import models
def agregarClaseFormControl(elementos):
    for campo in elementos:
        campo.field.widget.attrs['class'] = 'form-control'

class inicioForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(inicioForm,self).__init__(*args, **kwargs)
        agregarClaseFormControl(self.visible_fields())  
    class Meta:

        model = Usuario
        fields = ['usr_nombre','usr_apellido_pat','usr_apellido_mat','usr_correo','usr_pass']
        labels={
            'usr_nombre':'Nombre',
            'usr_apellido_pat':'Apellido Paterno',
            'usr_apellido_mat':'Apellido Materno',
            'usr_correo':'Correo',
            'usr_pass':'Contraseña',
        }
class direccionForm(ModelForm):
    class Meta:
        model = Direccion
        fields = ['dir_calle','dir_nro','dir_depto','dir_depto_nro','comuna_nombre']
        labels={
            'dir_calle':'Direccion',
            'dir_nro':'numero casa',
            'dir_depto':'es departamento',
            'dir_depto_nro':'numero departamento',

        }
        indexes=[
            models.Index(fields=['dir_comuna'], name='dir_comuna_id'),
        ]

class RegionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RegionForm,self).__init__(*args, **kwargs)
        agregarClaseFormControl(self.visible_fields())
    class Meta:
        model = Region
        fields = ['id_region']
        labels={
            'id_region':'Region',
        }
