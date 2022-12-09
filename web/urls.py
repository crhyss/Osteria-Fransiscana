from django.urls import path
from .views import vista_mesas, vista_mesero, agregar_prod, pedido_listo, terminar_venta, limpiar_mesa

urlpatterns = [
    path('vista_mesas/', vista_mesas, name="vista_mesas"),
    path('mesero/limpiar_mesa/<str:id_mesa>', limpiar_mesa, name="limpiar_mesa"),
    path('vista_mesero/<str:id_mesa>', vista_mesero, name="comenzar_venta"),
    path('vista_mesero/', agregar_prod),
    path('mesero/entregar_ped', pedido_listo),
    path('terminar_venta/', terminar_venta)
]