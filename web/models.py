from django.db import models
from cliente.models import Mesa

class Estado_venta(models.Model):
    id_estado_venta = models.AutoField(primary_key=True)
    estado_venta = models.CharField(max_length=20)

class Tipo_venta(models.Model):
    id_tipo_venta = models.AutoField(primary_key=True)
    tipo_venta = models.CharField(max_length=20)

class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    vta_fecha = models.DateTimeField(auto_created=True)
    vta_bruto = models.IntegerField(max_length=8, default=0)
    vta_iva = models.IntegerField(max_length=8, default=0)
    vta_propina = models.IntegerField(max_length=8, default=0)
    vta_final = models.IntegerField(max_length=8, default=0)
    vta_estado = models.ForeignKey(Estado_venta, on_delete= models.CASCADE)
    vta_tipo = models.ForeignKey(Tipo_venta, on_delete= models.CASCADE, blank=True)



