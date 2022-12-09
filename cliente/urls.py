from django.urls import include, path
from .views import salir, registro, carrito, pedido,addcart, mesero, reclamos, addDirec, listarReclamos, perfilCliente, modificarPerfil, reserva, entrar, cambiarContraseña, historialReservas,orders,deletecart

urlpatterns = [
    path('oauth/', include('social_django.urls', namespace='social')),
    path('salir/',salir, name='salir'),
    path('registro/',registro, name='registro'),
    path('registro/direccion', addDirec, name='DirecUsuario'),
    path('carrito/',carrito, name='carrito'),
    path('carrito/eliminar/',deletecart, name='deletecart'),
    path('carrito/agregar/',addcart,name="addcart"),
    path('orders/',orders,name='orders'),
    path('pedido/',pedido, name='pedido'),
    path('mesero/',mesero, name='mesero'),
    path('reclamo/',reclamos, name='reclamos'),
    path('reclamo/lista/',listarReclamos, name='reclamo_lista'),
    path('perfil/', perfilCliente, name='perfil'),
    path('modificarPerfil/<int:id_usuario>', modificarPerfil, name='modificar perfil'),
    path('reserva/<int:id_usuario>', reserva, name='reserva'),
    path('cambiarContraseña/<int:id_usuario>', cambiarContraseña, name='cambiar contraseña'),
    path('historialReservas/<int:id_usuario>', historialReservas, name='historial reservas'),
    path('login/', entrar, name='entrar')
]
