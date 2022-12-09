from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from.models import Rol,cupon
from productos.models import Producto,Categoria_prod
from django.utils.html import format_html
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.urls import path
from cliente.models import User,Reclamo,Tipo_usuario
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
class productosResourse(resources.ModelResource):
    Fields = ('id_producto','Imagen','prod_nombre','prod_descri','prod_precio_ba','prod_precio_of','prod_disponible','prod_recomendado','prod_categoria')
    class Meta:
        model = Producto
@admin.register(Producto)
class productoAdmin(ImportExportModelAdmin):
    resource_class = productosResourse
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

class userAdmin(admin.ModelAdmin):
    list_display=('id_user','user_nombre','user_apellidos','user_correo','user_tipo','is_active','is_staff')
    list_editable = ('user_correo','user_tipo','is_active','is_staff')
    def has_module_perms(self, request):
        return request.user.is_superuser

class ReclamoResourse(resources.ModelResource):
    Fields = ('id_reclamos','nombre','apellido','reclamo_fecha','reclamo_descrip')
    class Meta:
        model = Reclamo

class reclamoAdmin(ImportExportModelAdmin):
    
    resource_class = ReclamoResourse
    list_display=('id_reclamos','nombre','apellido','reclamo_fecha','reclamo_descrip')
    def get_model_perms(self, request):
        return {}

@admin.register(Tipo_usuario)       
class Tipo_usuarioAdmin(admin.ModelAdmin):
    list_display=('id_tipo_usr','tipo_usr')
admin.site.register(Reclamo, reclamoAdmin)
admin.site.register(User, userAdmin)

