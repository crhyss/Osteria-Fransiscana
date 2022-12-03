from django.urls import path
from .views import vista_mesas, vista_mesero, agregar_prod

urlpatterns = [
    path('vista_mesas/', vista_mesas, name="vista_mesas"),
    path('vista_mesero/<str:id_mesa>', vista_mesero),
    path('vista_mesero/', agregar_prod)
]