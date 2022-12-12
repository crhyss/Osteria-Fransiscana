from django.contrib import admin
from django.urls import include, path
from .views import paginaprincipal , ordenes, perfil, confirmacionDelivery, confirmacionRetiro, sobrenosotros,offline
from webpay_plus.routes import webpay_plus_create,commitpay
from administrador.views import grafico
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', paginaprincipal,name="loby"),
    path('logeo/', include('cliente.urls'),name="login"),
    path('productos/', include('productos.urls'),name="producto"),
    path('web/', include('web.urls'), name="mesero"),
    path('map/', include('map.urls'),name="mapa"),
    path('ordenes/', ordenes, name='ordenes'),
    path('accounts/profile/',perfil,name='perfil'),
    path('sobrenosotros/',sobrenosotros,name='sobrenosotros'),
    path('', include('administrador.urls'),name="administrador"),
    path('jet/', include('jet.urls','jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('webpay-plus/create/', webpay_plus_create,name="create"),
    path('webpay-plus/create/commit-pay/', commitpay),
    path('delivery/<int:id>',confirmacionDelivery,name="delivery" ),
    path('retiro/<int:id>',confirmacionRetiro,name="retiro" ),
    path('graficos/',grafico,name="grafico"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'osteleria.views.offline'
handler500 = 'osteleria.views.serve'