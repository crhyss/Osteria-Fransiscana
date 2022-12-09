from django.db import models
import datetime
from cliente.models import User

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
