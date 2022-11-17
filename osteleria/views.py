from django.http import HttpResponse
from django.shortcuts import render, redirect
from productos.models import Producto, Categoria_prod
from django.contrib.auth import models
from django.contrib.admin import ModelAdmin 

from django.utils.translation import gettext_lazy as _
from jet.dashboard.dashboard import Dashboard, AppIndexDashboard
from jet.dashboard.dashboard_modules import google_analytics


class CustomIndexDashboard(Dashboard):
    columns = 3

    def init_with_context(self, context):
       self.available_children.append(google_analytics.GoogleAnalyticsVisitorsTotals)
       self.available_children.append(google_analytics.GoogleAnalyticsVisitorsChart)
       self.available_children.append(google_analytics.GoogleAnalyticsPeriodVisitors)
def paginaprincipal(request):
    productos = Producto.objects.all()
    lista = Categoria_prod.objects.all()
    context = {
        'titulo': 'Productos',
        'productos': productos,
        'lista': lista,
    }
    return render(
        request,
        'vista/Principal.html',
        context
    )


def ordenes(request):
    return render(
        request, 
        'vista/ordenes.html'
    )

def perfil(request):
    usuarios = models.User.objects.all()
    grupos = models.Group.objects.all()
    permisos = models.Permission.objects.all()
    context = {
        'titulo': 'Usuario',
        'usuarios': usuarios,
        'grupos':grupos,
        'permisos':permisos,
    }
    return render(request, 'vista/Principal.html',context)
