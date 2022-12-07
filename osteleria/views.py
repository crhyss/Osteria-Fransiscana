from django.http import HttpResponse
from django.shortcuts import render, redirect
from productos.models import Producto, Categoria_prod
from cliente.models import User
from django.contrib.auth import models
from django.contrib.admin import ModelAdmin 
from web.models import Estado_venta,Seleccion,Carrito
def paginaprincipal(request):
    productos = Producto.objects.all()
    lista = Categoria_prod.objects.all()
    if request.user.is_authenticated:
        carrito = Carrito.llamar_carrito(request.user.id_user)
        listar= (Seleccion.objects.filter(id_carrito = carrito.id_carrito).select_related('id_prod')
        .values('id_seleccion','cantidad','id_prod__id_producto','id_prod__prod_nombre','id_prod__prod_imagen','id_prod__prod_precio_of','id_prod__id_producto')) 
        context = {
            'titulo': 'Productos',
            'productos': productos,
            'lista': lista,
            'carrito':carrito,
            'listar':listar
        }
        return render(
            request,
            'vista/Principal.html',
            context
        )
    else:
        
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
def sobrenosotros(request):
    return render(
        request, 
        'vista/sobrenosotros.html',
    )    
