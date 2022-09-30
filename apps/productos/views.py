from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Producto, Categoria_prod
from .forms import ProductoForm
def agregarp(request):
    lista = Categoria_prod.objects.all()
    formulario = None
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('/productos/listar/')
    else:
        formulario = ProductoForm()
    context = {
        'titulo': 'Agregar Producto',
        'formulario': formulario,
        'lista': lista,
    }
    return render(
        request,
        'web/crudProducto/agregarp.html',
        context
    )
def listarProducto(request):
    productos = Producto.objects.all()
    lista = Categoria_prod.objects.all()
    context = {
        'titulo': 'Productos',
        'productos': productos,
        'lista': lista,
    }
    return render(
        request,
        'web/crudProducto/listarMenu.html',
        context
    )
def modificarProducto(request, id_producto):
    productoRecibido = Producto.objects.get(pk=id_producto)
    lista = Categoria_prod.objects.all()
    formulario = None
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, instance=productoRecibido)
        if formulario.is_valid():
            formulario.save()
            return redirect('/productos/listar/')
    else:
        formulario = ProductoForm(instance=productoRecibido)
    context = {
        'titulo': 'Modificar Producto',
        'formulario': formulario,
        'lista': lista,
    }
    return render(
        request,
        'web/crudProducto/modificar.html',
        context
    )
def eliminarProducto(request, id_producto):
    productoEliminado = Producto.objects.get(pk=id_producto)
    productoEliminado.delete()
    return redirect('/productos/listar/')