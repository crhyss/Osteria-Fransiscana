from django.forms import ModelForm
from .models import Producto, Categoria_prod, Pedido

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

        labels={
            'prod_nombre':'Nombre',
            'prod_descri':'Descripción',
            'prod_precio_ba':'Precio Base',
            'prod_precio_of':'Precio Oferta',
            'prod_imagen':'Imagen',
            'prod_categoria':'Categoria'
        }

class CategoriaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CategoriaForm,self).__init__(*args, **kwargs)
        agregarClaseFormControl(self.visible_fields())
    class Meta:
        model = Categoria_prod
        fields = ['categoria_prod']

class PedidoForm_V(ModelForm):
    def __init__(self, *args, **kwargs):
      super(PedidoForm_V,self).__init__(*args, **kwargs)
      agregarClaseFormControl(self.visible_fields())
      self.fields['pedido_modif'].widget.attrs['disabled'] = 'disabled'

    class Meta:
        model = Pedido
        fields = ['pedido_modif']
        labels = {
            'pedido_modif' : 'Detalle'
        }

class PedidoForm(ModelForm):
    class Meta:
        model = Pedido
        fields = ['id_pedido', 'pedido_modif', 'pedido_listo', 'pedido_producto']

        labels={
            'id_pedido':'ID',
            'pedido_modif': 'Detalle',
            'pedido_listo' : 'Estado',
            'pedido_producto' : 'Producto'
        }