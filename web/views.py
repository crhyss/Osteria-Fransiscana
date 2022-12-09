from django.shortcuts import render, redirect
from cliente.models import Mesa, EstadoMesa, Local
from productos.models import Producto, Categoria_prod
from .models import Venta, Pedido
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def vista_mesas(request):
    mesas = Mesa.objects.all()
    estados = EstadoMesa.objects.all()
    locales = Local.objects.all()
    data = {
        "mesas":mesas,
        "estados": estados,
        "locales": locales
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
    venta = venta.calcular_venta()
    propina = round(venta.vta_final * 0.1)
    total = venta.vta_final + propina
    data = {
        "venta":venta,
        "mesa": mesa,
        "pedidos" : pedidos,
        "productos" : productos,
        "categorias" : categorias,
        "propina": propina,
        "total":total
    }
    return render(request, 'web/mesero/vista_mesero.html', data)

def agregar_prod(request):
    if request.method == "POST":
        pedido = Pedido.agregar_pedido(
            request.POST["modific"],
            request.POST["producto"],
            request.POST["id_venta"]
        )
    return render(request, 'web/mesero/vista_mesero.html')

def pedido_listo(request):
    if request.method == "POST":
        print(request.POST["id_pedido"])
        Pedido.entregar_pedido(request.POST["id_pedido"])
        return render(request, 'web/mesero/vista_mesero.html')

def terminar_venta(request):
    if request.method == "POST":
        venta = Venta.objects.get(id_venta = request.POST["venta_id"])
        venta.terminar_venta(request.POST["propina"], request.POST["TipoPago"])
    return render(request, 'web/mesero/vista_mesero.html')

def limpiar_mesa(request, id_mesa):
    mesa = Mesa.objects.get(id_mesa = int(id_mesa))
    print(mesa)
    mesa.mesa_limpia()
    return redirect('/web/vista_mesas/')