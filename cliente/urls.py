from django.urls import include, path
from .views import salir, registro, carrito, mesero, reclamos

urlpatterns = [
    path('oauth/', include('social_django.urls', namespace='social')),
    path('salir/',salir, name='salir'),
    path('registro/',registro, name='registro'),
    path('carrito/',carrito, name='carrito'),
    path('mesero/',mesero, name='mesero'),
    path('reclamo/',reclamos, name='reclamos'),
    
]
