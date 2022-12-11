from cliente.models import User
from productos.models import Producto
from django.db import models
from cliente.models import Mesa, EstadoMesa

class Carrito(models.Model):
    id_carrito = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(User, on_delete= models.CASCADE)
    def agregar_prod(id_usuario, id_prod):
        carrito = Carrito.llamar_carrito(id_usuario)
        try:
            select = Seleccion.objects.get(id_carrito = carrito.id_carrito, id_prod_id = id_prod)
            select.cantidad = select.cantidad + 1
            select.save()
        except:
            select = Seleccion()
            select.id_prod = Producto.objects.get(id_producto = id_prod)
            select.id_carrito = Carrito.objects.get(id_carrito = carrito.id_carrito)
            select.save()

    def eliminar_prod(id_carrito, id_prod):
        Seleccion.objects.get(id_carrito = id_carrito, id_prod = id_prod).delete()

    def eliminar_carrrito(id_carrito):
        Seleccion.objects.filter(id_carrito_id=id_carrito).delete()
    def listar_prod(id_usuario):
        carrito = Carrito.llamar_carrito(id_usuario)
        select = Seleccion.objects.filter(id_carrito = carrito.id_carrito)
        return select
    @staticmethod
    def llamar_carrito(id_usuario):
        try:
            carrito = Carrito.objects.get(id_usuario = id_usuario)
        except:
            carrito = Carrito()
            carrito.id_usuario = User.objects.get(id_user = id_usuario)
            carrito.save()
        return carrito
class Seleccion(models.Model):
    id_seleccion = models.AutoField(primary_key=True)
    id_prod = models.ForeignKey(Producto, on_delete= models.CASCADE, blank=False)
    cantidad = models.IntegerField(default=1)
    id_carrito = models.ForeignKey(Carrito, on_delete= models.CASCADE)


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
        mesa = Mesa.objects.get(id_mesa = id_mesa)
        venta.vta_estado = Estado_venta.objects.get(id_estado_venta = 1)
        venta.vta_tipo = Tipo_venta.objects.get(id_tipo_venta = 1)
        venta.vta_mesa = mesa
        mesa.mesa_estado = EstadoMesa.objects.get(id_estado_mesa = 2)
        venta.save()
        mesa.save()
        return venta
    def nueva_venta_online(id_mesa):
        venta = Venta()
        mesa = Mesa.objects.get(id_mesa = id_mesa)
        venta.vta_estado = Estado_venta.objects.get(id_estado_venta = 1)
        venta.vta_tipo = Tipo_venta.objects.get(id_tipo_venta = 1)
        venta.vta_mesa = mesa
        mesa.mesa_estado = EstadoMesa.objects.get(id_estado_mesa = 2)
        venta.save()
        mesa.save()
        return venta
    def venta_retiro(bruto,date,vta_tipo_id):
        venta = Venta()
        venta.vta_estado = Estado_venta.objects.get(id_estado_venta = 1)
        venta.vta_tipo = Tipo_venta.objects.get(id_tipo_venta = vta_tipo_id)
        a = round((bruto * 100)/119)
        venta.vta_bruto = round((bruto * 100)/119)
        venta.vta_fecha = date
        venta.vta_iva = bruto - a
        if vta_tipo_id == 2:
            venta.vta_propina = 3500
            venta.vta_final = bruto + 3500
            venta.save()
            return venta    
        else:
            venta.vta_propina = 0
            venta.vta_final = bruto + 0
            venta.save()
            return venta    
    
    def calcular_venta(self):
        total = 0
        bruto = 0
        iva = 0
        listar = (Pedido.objects.filter(pedido_venta = self.id_venta).select_related('pedido_producto')
        .values('id_pedido','pedido_producto__id_producto','pedido_producto__prod_nombre','pedido_producto__prod_precio_ba','pedido_producto__prod_precio_of','pedido_producto__id_producto'))
        for producto in listar:
            precio_base = producto.get("pedido_producto__prod_precio_ba")
            precio_oferta = producto.get("pedido_producto__prod_precio_of")
            if precio_base >= precio_oferta:
                total += precio_oferta
            else:
                total += precio_base
        bruto = round((total * 100)/119)
        iva = total - bruto
        self.vta_bruto = bruto
        self.vta_iva = iva
        self.vta_final = total
        self.save()
        return self

    def terminar_venta(self, propina, estado_venta):
        self.vta_propina = int(propina)
        self.vta_final = self.vta_final + self.vta_propina
        self.vta_estado = Estado_venta.objects.get(id_estado_venta = estado_venta)
        estado = EstadoMesa.objects.get(id_estado_mesa = 3)
        mesa = Mesa.objects.get(id_mesa = self.vta_mesa_id)
        mesa.mesa_estado = estado
        mesa.save()
        self.save()

class Estado_pedido(models.Model):
    id_estado_pedido = models.AutoField(primary_key=True)
    estado_pedido = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.estado_pedido

class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    pedido_modif = models.CharField(max_length=200, blank=False)
    pedido_estado = models.ForeignKey(Estado_pedido, on_delete= models.CASCADE, default=1)
    pedido_producto = models.ForeignKey(Producto, on_delete=models.CASCADE, default=None)
    pedido_venta = models.ForeignKey(Venta, on_delete= models.CASCADE)

    def agregar_pedido(pedido_modif, pedido_prod, id_venta):
        pedido = Pedido()
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

    def entregar_pedido(id_pedido):
        pedido = Pedido.objects.get(id_pedido = id_pedido)
        estado = Estado_pedido.objects.get(id_estado_pedido = 3)
        pedido.pedido_estado = estado
        pedido.save()
        return pedido

