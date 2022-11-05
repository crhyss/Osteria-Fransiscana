from django.contrib import admin
from django.urls import include, path
from .views import agregarp, listarProducto, modificarProducto, eliminarProducto, cancelarPedido, visualizarPedido, terminarPedido, pedidos

urlpatterns = [
    path('agregarp/', agregarp,name="agregarp"),
    path('listar/', listarProducto, name="listar"),
    path('modificar/<int:id_producto>', modificarProducto, name='modificar'),
    path('pedidos/', pedidos, name='pedidos'),
    path('eliminar/<int:id_producto>', eliminarProducto, name='eliminar'),
    path('cancelar/<int:id_pedido>', cancelarPedido, name='cancelar' ),
    path('pedidos/visualizar/<int:id_pedido>', visualizarPedido, name='finalizar'),
    path('pedidos/terminar/<int:id_pedido>', terminarPedido, name='terminar' )
]
