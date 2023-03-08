from django.views.generic.edit import CreateView
from .models import map
from web.models import Carrito,Seleccion
# Create your views here.

class MapView(CreateView):
    model = map
    fields = ['address']
    template_name = 'map/map.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mapbox_access_token'] = 'pk.eyJ1IjoiY3JhdXoiLCJhIjoiY2w0dzZjZWk5MjV4eTNqczg2bmIwazNoMCJ9.VaYyChMCUOnf5dJjUhDwDg'
        context['addresses'] = map.objects.all()

        if self.request.user.is_authenticated:
            carrito = Carrito.llamar_carrito(self.request.user.id_user)
            listar = (Seleccion.objects.filter(id_carrito=carrito.id_carrito)
                      .select_related('id_prod')
                      .values('id_seleccion', 'cantidad', 'id_prod__id_producto', 'id_prod__prod_nombre',
                              'id_prod__prod_imagen', 'id_prod__prod_precio_of', 'id_prod__id_producto'))
        else:
            carrito = None
            listar = None

        context.update({
            'carrito': carrito,
            'listar': listar
        })

        return context