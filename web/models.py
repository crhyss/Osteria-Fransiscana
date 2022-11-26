# from cliente.models import Usuario
# from productos.models import Producto
# from django.db import models

# class Carrito(models.Model):
#     id_carrito = models.AutoField(primary_key=True)
#     id_usuario = models.ForeignKey(Usuario, on_delete= models.CASCADE)
#     def agregar_prod(id_carrito, id_prod):
#         try:
#             select = Seleccion.objects.get(id_carrito = id_carrito, id_prod = id_prod)
#             select.cantidad = select.cantidad + 1
#         except:
#             select = Seleccion()
#             select.id_prod(id_prod)
#             select.id_carrito(id_carrito)
#             select.save()
#     def eliminar_prod(id_carrito, id_prod):
#         Seleccion.objects.delete(id_carrito = id_carrito, id_prod = id_prod)
#     def listar_prod(id_carrito):
#         select = Seleccion.objects.get(id_carrito = id_carrito)
#         return select

# class Seleccion(models.Model):
#     id_seleccion = models.AutoField(primary_key=True)
#     id_prod = models.ForeignKey(Producto, on_delete= models.CASCADE, blank=False)
#     cantidad = models.IntegerField(default=0)
#     id_carrito = models.ForeignKey(Carrito, on_delete= models.CASCADE)

