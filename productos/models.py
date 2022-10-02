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
    prod_imagen    = models.FileField(upload_to='media/%Y/%m/%d/', default=None)
    prod_categoria = models.ForeignKey(Categoria_prod, on_delete=models.CASCADE, default=None)