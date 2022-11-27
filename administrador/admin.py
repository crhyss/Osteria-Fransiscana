from django.contrib import admin
from.models import Rol,cupon,Boleta,Tipo_venta,Estado_venta
from productos.models import Producto,Categoria_prod
from django.utils.html import format_html
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.urls import path

class MyModelAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('my_view/', self.admin_site.admin_view(self.my_view))
        ]
        return my_urls + urls
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
    list_display = ('id_producto','Imagen','prod_nombre','prod_descri','prod_precio_ba','prod_precio_of','prod_disponible','prod_recomendado','prod_categoria')
    list_display_links = ('prod_nombre',)
    list_editable = ('prod_disponible','prod_recomendado','prod_categoria','prod_precio_of')
    list_per_page = 6
    search_fields = (
        "prod_nombre",
        "prod_categoria__categoria_prod",
    )
    def Imagen(self,obj):
        return format_html('<img src ={} width="100" height="100"/>',obj.prod_imagen.url)
@admin.register(Categoria_prod)
class categoriaAdmin(admin.ModelAdmin):
    list_display = ('categoria_prod',)
@admin.register(cupon)
class cuponAdmin(admin.ModelAdmin):
    list_display=('id_cupon','Nombre_cupon','cantidad','Monto')

@admin.register(Boleta)
class BoletaAdmin(admin.ModelAdmin):
    list_display=('nro_orden','bta_fecha','cantidad_prod','productos','bta_Total','id_tipo_boleta','id_estado_boleta','id_Usuario_boleta')
@admin.register(Tipo_venta)
class Tipo_venta_BAdmin(admin.ModelAdmin):
    list_display=('id_tipo_venta','tipo_venta')
@admin.register(Estado_venta)
class Estado_ventaAdmin(admin.ModelAdmin):
    list_display=('id_estado','Estado_venta')