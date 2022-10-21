from multiprocessing import context
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from cliente.forms import inicioForm,direccionForm
from cliente.models import Direccion, Region, Comuna
from django.contrib.auth.forms import AuthenticationForm
import json


def registro(request):
    if request.method == 'POST':
        formulario = inicioForm(request.POST, request.FILES)
        formulario2= direccionForm(request.POST, request.FILES)
        comuna = Comuna.objects.all()
        region = Region.objects.all()
        if formulario2.is_valid():
            print(formulario2)
            print('holaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
            formulario2.save()
            formularioRegistrado = formulario.save(commit=False)   
            formularioRegistrado.usr_direccion = formulario2.codigo_postal
            formulario.save()
            return redirect('/productos/listar/')
    else:
        formulario = inicioForm()
        formulario2 = direccionForm()
        comuna = Comuna.objects.all()
        region = Region.objects.all()
    context = {
        'titulo': 'Agregar Producto',
        'formulario': formulario,
        'formulario2': formulario2,
        'comuna':comuna,
        'region': region,
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

