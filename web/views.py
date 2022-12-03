from django.shortcuts import render
from cliente.models import Mesa, EstadoMesa
from productos.models import Producto, Categoria_prod
from .models import Venta, Pedido
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def vista_mesas(request):
    mesas = Mesa.objects.all()
    estados = EstadoMesa.objects.all()
    data = {
        "mesas":mesas,
        "estados": estados
    }
    return render(request, "web/mesero/vista_mesas.html", data)

def vista_mesero(request, id_mesa):
    categorias = Categoria_prod.objects.all()
    productos = Producto.objects.filter(prod_disponible = True)
    try:
        venta = Venta.objects.get(vta_mesa = id_mesa, vta_estado = 1)
    except:
        venta = Venta.nueva_venta_local(id_mesa)
    pedidos = Pedido.obtener_pedidos(venta.id_venta)
    mesa = Mesa.objects.get(id_mesa = id_mesa)
    if request.method == "POST":
        print("uwu")

    data = {
        "venta":venta,
        "mesa": mesa,
        "pedidos" : pedidos,
        "productos" : productos,
        "categorias" : categorias
    }
    return render(request, 'web/mesero/vista_mesero.html', data)

def agregar_prod(request):
    if request.method == "POST":
        print(request.POST["modific"])
        pedido = Pedido.agregar_pedido(
            request.POST["modific"],
            request.POST["producto"],
            request.POST["id_venta"]
        )
        print(pedido)
    return render(request, 'web/mesero/vista_mesero.html')
