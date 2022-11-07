from multiprocessing import context
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from cliente.forms import inicioForm,direccionForm,RegionForm,ComunaForm, CalleForm,CalleComForm,CalleRegForm
from cliente.models import Direccion, Region, Comuna
from django.contrib.auth.forms import AuthenticationForm
import json


def registro(request):
    a = request.POST
    form = CalleComForm()
    form2= CalleRegForm()
    if request.method == 'POST':
        form = CalleComForm(request.POST)
        form2 = CalleRegForm(request.POST)
        formulario2= direccionForm(request.POST, request.FILES)
        comuna = Comuna.objects.all()
        region = Region.objects.all()
        print(a)
        if formulario2.is_valid():
            print('holaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
            formulario2.save()
        return redirect('/logeo/registro')
    else:
        formulario = inicioForm()
        formulario2 = direccionForm()
        comuna = Comuna.objects.all()
        region = Region.objects.all()

    context = {
        'titulo': 'Agregar Producto',
        'formulario2': formulario2,
        'comuna':comuna,
        'region': region,
        'form':form,
        'form2':form2,
    }
    return render(request, 'registration/registro.html', context)




def salir(request):
    logout(request)
    return redirect(to='loby')


def carrito(request):
    return render(request, 'carrito/carrito.html')


def mesero(request):
    return render(request, 'test/vistamesero.html')


def reclamos(request):
    archivo_json = 'templates/json/comentarios.json'
    if request.method == 'POST':
        comentarios = request.POST
        with open(archivo_json, "r+") as file:
            data = json.load(file)
            data.append(comentarios)
            file.seek(0)
            json.dump(data, file)
            file.close()
        return render(request, 'web/vista/reclamos.html')

