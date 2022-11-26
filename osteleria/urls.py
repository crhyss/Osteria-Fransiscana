"""osteleria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from .views import paginaprincipal , ordenes, perfil
from webpay_plus.routes import webpay_plus_create,commitpay

urlpatterns = [
    path('', paginaprincipal,name="loby"),
    path('logeo/', include('cliente.urls'),name="login"),
    path('productos/', include('productos.urls'),name="producto"),
    path('map/', include('map.urls'),name="mapa"),
    path('ordenes/', ordenes, name='ordenes'),
    path('accounts/', include('django.contrib.auth.urls'),name="login"),
    path('accounts/profile/',perfil,name='perfil'),
    path('', include('administrador.urls'),name="administrador"),
    path('jet/', include('jet.urls','jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('webpay-plus/create/', webpay_plus_create,name="create"),
    path('webpay-plus/commit-pay/', commitpay),
]