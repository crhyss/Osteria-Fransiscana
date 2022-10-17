from django.http import HttpResponse
from django.shortcuts import render, redirect
from productos.models import Producto, Categoria_prod

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
    return render(
        request, 
        'vista/Principal.html'
    )
