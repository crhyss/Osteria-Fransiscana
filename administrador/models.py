from django.db import models
import datetime
from cliente.models import User
# Create your models here.
class Rol(models.Model):
    id_rol = models.AutoField(primary_key = True)
    rol = models.CharField( max_length=50)
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.id_rol,self.rol)
     
class cupon(models.Model):
    id_cupon = models.AutoField(primary_key = True)
    Nombre_cupon = models.CharField(max_length=12)
    cantidad = models.PositiveIntegerField()
    Monto = models.PositiveIntegerField()

class Tipo_venta(models.Model):
    id_tipo_venta = models.AutoField(primary_key = True)
    tipo_venta = models.CharField(max_length=50)
    def __str__(self):
        return self.tipo_venta
class Estado_venta(models.Model):
    id_estado = models.AutoField(primary_key = True)
    Estado_venta = models.CharField(max_length=50)
    def __str__(self):
        return self.Estado_venta
class Boleta(models.Model):
    nro_orden = models.AutoField(primary_key = True)
    bta_fecha = models.DateTimeField(blank=True, null=True, default=(datetime.datetime.now()))
    cantidad_prod = models.PositiveIntegerField()
    productos = models.CharField(max_length=50)
    bta_Total = models.PositiveIntegerField()
    id_tipo_boleta = models.ForeignKey(Tipo_venta,on_delete=models.CASCADE, default=None)
    id_estado_boleta = models.ForeignKey(Estado_venta,on_delete=models.CASCADE, default=None)
    id_Usuario_boleta = models.ForeignKey(User,on_delete=models.CASCADE, default=None)
