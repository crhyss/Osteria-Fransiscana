from django.urls import include, path
from .views import administrador

urlpatterns = [
    path('admin/', administrador, name='admin'),
    ]

