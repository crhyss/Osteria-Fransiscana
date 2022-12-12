from django.urls import include, path
from .views import prediccion

urlpatterns = [
    path('prediccion/', prediccion, name='prediccion')

    ]

