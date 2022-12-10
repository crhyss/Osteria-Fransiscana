from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Producto, Categoria_prod
from web.models import Pedido
from .forms import ProductoForm#, PedidoForm, PedidoForm_V
from django.core.paginator import Paginator

def agregarp(request):
    lista = Categoria_prod.objects.all()
    productos = Producto.objects.all()
    lista2 = Categoria_prod.objects.all()
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
        'productos': productos,
        'lista2': lista2,
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

def pedidos(request):
    data = {
        'pedidos' : Pedido.objects.filter(pedido_listo = 0)
    }
    return render(
        request, 
        'vista/pedidos.html',
        data
    )

def historialPedido(request):
    data = {
        'pedidos' : Pedido.objects.filter(pedido_listo = 1)
    }
    return render(
        request, 
        'vista/historialPedidos.html',
        data
    )

def cancelarPedido(request, id_pedido):
    pedidoCancelado = Pedido.objects.get(pk=id_pedido)
    pedidoCancelado.pedido_listo = 1
    pedidoCancelado.save()
    return redirect('/productos/pedidos/')

def eliminarPedido(request, id_pedido):
    pedidoCancelado = Pedido.objects.get(pk=id_pedido)
    pedidoCancelado.delete()
    return redirect('/productos/pedidos/historial')

def visualizarPedido(request, id_pedido):
    """
    pedidoVisualizado = Pedido.objects.get(pk=id_pedido)
    formularioPedido = None
    if request.method == 'POST':
        formularioPedido = PedidoForm_V(request.POST, instance=pedidoVisualizado)
        if formularioPedido.is_valid():
            formularioPedido.save()
            return redirect('/productos/pedidos/')
    else:
        formularioPedido = PedidoForm_V(instance=pedidoVisualizado)
    context = {
        'titulo': 'Visualizar Pedido',
        'formulario': formularioPedido
    }"""
    return render(
        request,
        'vista/visualizarPedido.html',
    )

def terminarPedido(request, id_pedido):
    pedidoTerminado = Pedido.objects.get(pk=id_pedido) 
    pedidoTerminado.pedido_listo = 1
    pedidoTerminado.save()
    return redirect('/productos/pedidos')
