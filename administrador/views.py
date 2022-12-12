from django.shortcuts import render
from django.db.models import Count
from cliente.models import User
from productos.models import Producto
from .forms import ProductoForm
from joblib import load 
import sys
from django.contrib.auth.decorators import user_passes_test
from web.models import Venta
def usuarioAdministrador(user):
    return user.user_tipo_id == 2

@user_passes_test(usuarioAdministrador)
def grafico(request):
    tipoVentaxventa = (Venta.objects.all().select_related('vta_tipo')
    .values('vta_tipo','vta_tipo__tipo_venta')
    .annotate(dcount=Count('vta_tipo')))
    cu = User.objects.all().count()
    tv = Venta.objects.all().count()
    #results = Members.objects.raw('SELECT * FROM myapp_members GROUP BY designation')
    productos = Producto.objects.all()
    categoriaxprod = (Producto.objects.all().select_related('categoria_prod')
    .values('prod_categoria','prod_categoria__categoria_prod')
    .annotate(dcount=Count('prod_categoria')))

    if request.method =='POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
    else:
        formulario = ProductoForm()
    context={
        'cu':cu,
        'tv':tv,
        'productos':productos,
        'categoriaProd':categoriaxprod,
        'form':formulario,
        'ventasxti':tipoVentaxventa,
    }
    return render(request, 'grafico/graficos.html',context)
@user_passes_test(usuarioAdministrador)
def prediccion(request):
    print(sys.argv[1:])
    predict_model = load("/Modelo/modelo_final.joblib")
    if request.method == 'GET':
        return render(request, "vista/prediccion.html")
    elif request.method == 'POST':
        Cantidad = int((request.POST['Cantidad']))
        Mes = int((request.POST['Mes']))
        Dia = int((request.POST['Dia']))
        print(Cantidad)
        salida = {
            "predict": int(predict_model.predict(([[Cantidad ,Mes, Dia]]))[0])
        }
        print(salida)
        return render(request, "vista/prediccion.html", context = salida)
    salida = salida.cleaned_data()
    salida = salida.save()