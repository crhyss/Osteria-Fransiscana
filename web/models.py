from django.db import models
from cliente.models import User
from productos.models import Producto
from cliente.models import Mesa

class Estado_venta(models.Model):
    id_estado_venta = models.AutoField(primary_key=True)
    estado_venta = models.CharField(max_length=20)

class Tipo_venta(models.Model):
    id_tipo_venta = models.AutoField(primary_key=True)
    tipo_venta = models.CharField(max_length=20)

class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    vta_fecha = models.DateTimeField(auto_now=True)
    vta_bruto = models.IntegerField(default=0)
    vta_iva = models.IntegerField(default=0)
    vta_propina = models.IntegerField(default=0)
    vta_final = models.IntegerField(default=0)
    vta_estado = models.ForeignKey(Estado_venta, on_delete= models.CASCADE)
    vta_tipo = models.ForeignKey(Tipo_venta, on_delete= models.CASCADE, blank=True)
    vta_mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE, blank=True, null=True)
    def nueva_venta_local(id_mesa):
        venta = Venta()
        venta.vta_estado = Estado_venta.objects.get(id_estado_venta = 1)
        venta.vta_tipo = Tipo_venta.objects.get(id_tipo_venta = 1)
        venta.vta_mesa = Mesa.objects.get(id_mesa = id_mesa)
        venta.save()
        return venta


class Carrito(models.Model):
    id_carrito = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(User, on_delete= models.CASCADE)
    def llamar_carrito(id_usuario):
        try:
            carrito = Carrito.objects.get(id_usuario = id_usuario)
        except:
            carrito = Carrito()
            carrito.id_usuario = User.objects.get(id_user = id_usuario)
            carrito.save()
        return carrito
    def agregar_prod(self, id_carrito, id_prod):
        try:
            select = Seleccion.objects.get(id_carrito = id_carrito, id_prod = id_prod)
            select.cantidad = select.cantidad + 1
        except:
            select = Seleccion()
            select.id_prod = Producto.objects.get(id_prod = id_prod)
            select.id_carrito = Carrito.objects.get(id_carrito = id_carrito)
            select.save()
    def eliminar_prod(id_carrito, id_prod):
        Seleccion.objects.delete(id_carrito = id_carrito, id_prod = id_prod)
    def listar_prod(id_carrito):
        select = Seleccion.objects.get(id_carrito = id_carrito)
        return select

class Seleccion(models.Model):
    id_seleccion = models.AutoField(primary_key=True)
    id_prod = models.ForeignKey(Producto, on_delete= models.CASCADE, blank=False)
    cantidad = models.IntegerField(default=0)
    id_carrito = models.ForeignKey(Carrito, on_delete= models.CASCADE)

class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    pedido_modif = models.CharField(max_length=200, blank=False)
    pedido_listo = models.BooleanField(default=False)
    pedido_producto = models.ForeignKey(Producto, on_delete=models.CASCADE, default=None)
    pedido_venta = models.ForeignKey(Venta, on_delete= models.CASCADE)

    def agregar_pedido(pedido_modif, pedido_prod, id_venta):
        pedido = Pedido()
        print("Pintamos toda la casa")
        pedido.pedido_modif = pedido_modif
        pedido.pedido_producto = Producto.objects.get(id_producto = pedido_prod)
        pedido.pedido_venta = Venta.objects.get(id_venta = id_venta)
        pedido.save()
        return pedido

    def obtener_pedidos(id_venta):
        try:
            pedido = Pedido.objects.filter(pedido_venta = id_venta)
        except:
            pedido = None
        return pedido





