from django.shortcuts import render
from django.db.models import Count
from cliente.models import User
from productos.models import Producto
from .forms import ProductoForm
def grafico(request):
    cu = User.objects.all().count()
    #results = Members.objects.raw('SELECT * FROM myapp_members GROUP BY designation')
    productos = Producto.objects.all()
    categoriaxprod = (Producto.objects.all().select_related('categoria_prod')
    .values('prod_categoria','prod_categoria__categoria_prod')
    .annotate(dcount=Count('prod_categoria'))
)
    if request.method =='POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
    else:
        formulario = ProductoForm()
    context={
        'cu':cu,
        'productos':productos,
        'categoriaProd':categoriaxprod,
        'form':formulario
    }
    return render(request, 'grafico/graficos.html',context)