from django.contrib import admin
from django.urls import include, path
from .views import agregarp, listarProducto, modificarProducto, eliminarProducto

urlpatterns = [
    path('agregarp/', agregarp,name="agregarp"),
    path('listar/', listarProducto, name="listar"),
    path('modificar/<int:id_producto>', modificarProducto, name='modificar'),
    path('eliminar/<int:id_producto>', eliminarProducto, name='eliminar'),
]
