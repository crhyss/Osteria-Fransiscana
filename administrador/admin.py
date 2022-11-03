from django.contrib import admin
from.models import Rol,cupon
from productos.models import Producto,Categoria_prod
# Register your models here.
@admin.register(Rol)
class rolAdmin(admin.ModelAdmin):
    list_display = ('id_rol','rol')
    #ordering = ('id_rol','rol')
    search_fields = ('id_rol','rol')
    list_editable = ('rol',)
#admin.site.register(rol_usuario,rolAdmin)
@admin.register(Producto)
class productoAdmin(admin.ModelAdmin):
    list_display = ('id_producto','prod_nombre','prod_descri','prod_precio_ba','prod_precio_of','prod_imagen','prod_disponible','prod_recomendado','prod_categoria')
    list_display_links = ('prod_nombre',)
    list_editable = ('prod_disponible','prod_recomendado','prod_categoria')
@admin.register(Categoria_prod)
class categoriaAdmin(admin.ModelAdmin):
    list_display = ('categoria_prod',)
@admin.register(cupon)
class cuponAdmin(admin.ModelAdmin):
    list_display=('id_cupon','Nombre_cupon','cantidad','Monto')