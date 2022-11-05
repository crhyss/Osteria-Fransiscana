from email.policy import default
from django.db import models

# Create your models here.
class Categoria_prod(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    categoria_prod = models.CharField(max_length=40, blank=False)
    def __str__(self):
        return self.categoria_prod

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    prod_nombre = models.CharField(max_length=100, blank=False)
    prod_descri = models.CharField(max_length=200, blank=False)
    prod_precio_ba = models.IntegerField(blank=False)
    prod_precio_of = models.IntegerField(blank=False)
    prod_imagen    = models.FileField(upload_to='productos/', default=None)
    prod_disponible = models.BooleanField(default = True)
    prod_recomendado = models.BooleanField(default=False)
    prod_categoria = models.ForeignKey(Categoria_prod, on_delete=models.CASCADE, default=None)
    def delete(self, *args, **kwargs):
        if self.prod_imagen:
            self.prod_imagen.delete()
        super().delete(*args, **kwargs)

class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    pedido_modif = models.CharField(max_length=200, blank=False)
    pedido_listo = models.BooleanField(default=False)
    pedido_producto = models.ForeignKey(Producto, on_delete=models.CASCADE, default=None)