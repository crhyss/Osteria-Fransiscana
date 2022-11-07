
from importlib.metadata import requires
from tkinter import Widget
from django import forms
from .models import Usuario, Direccion, Region, Reserva
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

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
        model = Usuario
        fields = ['usr_nombre', 'usr_apellido_pat', 'usr_apellido_mat',
                  'usr_pass', 'usr_correo']

        labels = {
            'usr_nombre' : 'Nombre',
            'usr_apellido_pat' : 'Apellido Paterno',
            'usr_apellido_mat' : 'Apellido Materno',
            'usr_pass' : 'Contraseña',
            'usr_correo' : 'Correo',
        }

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


