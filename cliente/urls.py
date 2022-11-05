from django.urls import include, path
from .views import salir, registro, carrito, mesero, reclamos, addDirec, perfilCliente, modificarPerfil

urlpatterns = [
    path('oauth/', include('social_django.urls', namespace='social')),
    path('salir/',salir, name='salir'),
    path('registro/',registro, name='registro'),
    path('registro/direccion', addDirec, name='DirecUsuario'),
    path('carrito/',carrito, name='carrito'),
    path('mesero/',mesero, name='mesero'),
    path('reclamo/',reclamos, name='reclamos'),
    path('perfil/', perfilCliente, name='perfil'),
    path('modificarPerfil/<int:id_usuario>', modificarPerfil, name='modificar perfil')
]
