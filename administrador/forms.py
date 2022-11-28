from django import forms
from django.forms import ModelForm
from productos.models import Producto


class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields='__all__'
        widgets = {
            'prod_categoria': forms.TextInput(attrs={'class':'form-control'}),
            'prod_nombre': forms.TextInput(attrs={'class':'form-control'})
        }