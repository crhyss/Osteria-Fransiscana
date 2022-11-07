
from select import select
from tkinter.tix import Select
from .models import Usuario, Direccion, Comuna,Region
from django.forms import ModelForm,EmailInput,ModelChoiceField,Form,TextInput,Textarea
from django.contrib import admin
from django import forms
from django.db import models
from django.forms.models import ModelChoiceIterator
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
        fields = ['dir_calle','dir_nro','dir_depto','dir_depto_nro','dir_comuna']
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
        fields = ['id_region','region_nombre']
        labels={
            'id_region':'Region',
        }
class ComunaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ComunaForm,self).__init__(*args, **kwargs)
        agregarClaseFormControl(self.visible_fields())
    class Meta:
        model = Comuna
        fields = ['id_comuna','comuna_nombre','comuna_region']
        labels={
            'id_comuna':'comuna',
        }

class CalleForm(forms.Form):
    comuna = forms.ModelChoiceField(
        label=u'Comuna',
        queryset=Comuna.objects.all()
    )
    region =forms.ModelChoiceField(
        label=u'Region',
        queryset=Region.objects.all()
    )
    direccion = forms.ModelChoiceField(
        label=u'Direccion',
        queryset=Direccion.objects.all()
    )
    def __init__(self,*args,**kwargs):
        super(CalleForm,self).__init__(*args, **kwargs)
class ToppingSelect(forms.Select):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex, attrs)
        if value:
            option['attrs']['Id_comuna'] = value.instance.comuna_region
        return option       
class CalleComForm(forms.Form):
    comuna = forms.ModelChoiceField(
    queryset=Comuna.objects.all(),
    label='Comuna',
    empty_label= 'Seleccione una Comuna',
    to_field_name='id_comuna',
    widget= ToppingSelect,
)
class regionSelect(forms.Select):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex, attrs)
        if value:
            option['attrs']['id_region'] = value.instance.id_region
        return option       
class CalleRegForm(forms.Form):

    region = forms.ModelChoiceField(
    queryset=Region.objects.all(),
    label='Region',
    widget= regionSelect,
    to_field_name='region_nombre',
    empty_label= 'Seleccione una Region',
    

)       


    