from django.forms import ModelForm
from .models import Producto, Categoria_prod

def agregarClaseFormControl(elementos):
    for campo in elementos:
        campo.field.widget.attrs['class'] = 'form-control'
class ProductoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductoForm,self).__init__(*args, **kwargs)
        agregarClaseFormControl(self.visible_fields())  
    class Meta:
        model = Producto
        fields = ['prod_nombre','prod_descri','prod_precio_ba','prod_precio_of','prod_imagen','prod_categoria']

class CategoriaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CategoriaForm,self).__init__(*args, **kwargs)
        agregarClaseFormControl(self.visible_fields())
    class Meta:
        model = Categoria_prod
        fields = ['categoria_prod']