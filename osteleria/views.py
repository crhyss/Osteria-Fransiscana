from django.http import HttpResponse
from django.shortcuts import render, redirect
from productos.models import Producto, Categoria_prod
from cliente.models import User
from django.contrib.auth import models
from django.contrib.admin import ModelAdmin 
from administrador.models import Estado_venta
def paginaprincipal(request):
    productos = Producto.objects.all()
    lista = Categoria_prod.objects.all()
    context = {
        'titulo': 'Productos',
        'productos': productos,
        'lista': lista,
    }
    return render(
        request,
        'vista/Principal.html',
        context
    )


def ordenes(request):
    return render(
        request, 
        'vista/ordenes.html'
    )

def perfil(request):
    usuarios = User.objects.all()
    grupos = models.Group.objects.all()
    permisos = models.Permission.objects.all()
    context = {
        'titulo': 'Usuario',
        'usuarios': usuarios,
        'grupos':grupos,
        'permisos':permisos,
    }
    return render(request, 'vista/Principal.html',context)

def confirmacionDelivery(request,id):
    estado = Estado_venta.objects.get(pk=id)
    context = {
        'estado': estado,

    }
    return render(
        request, 
        'carrito/confirmacion-delivery.html',context
    )    
def confirmacionRetiro(request,id):
    estado = Estado_venta.objects.get(pk=id)
    context = {
        'estado': estado,

    }
    return render(
        request, 
        'carrito/confirmacion-retiro.html',context
    )    
