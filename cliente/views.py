from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from cliente.forms import direccionForm, userForm,reclamoForm
#, direccionForm
from cliente.models import Direccion, Region, Reclamo
from django.contrib.auth.forms import AuthenticationForm
import json


def registro(request):
    data = {
        'formulario': userForm()
    }
    if request.method == 'POST':
        
        formulario = userForm(data=request.POST)
        if formulario.is_valid():
            if request.POST["usr_pass"] and request.POST["confPass"]:
                formulario.save()
                print("Felicidades")
                messages.success(request, "registrado")
                return redirect(to='perfil')
            else:
                print("malulo")
        """

            formulario.save()
            user = authenticate(
                username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            
            
        data["formulario"] = formulario"""
    return render(request, 'registration/registro.html', data)

def addDirec(request):
    data = {
        'formulario':direccionForm,
        'regiones': Region.objects.all()
    }
    if request.method == 'POST':
        formulario = direccionForm(data=request.POST)
        if formulario.is_valid():
            print(request.POST["region"])
            
    return render(request, 'registration/registroDir.html', data)


def salir(request):
    logout(request)
    return redirect(to='loby')


def carrito(request):
    return render(request, 'carrito/carrito.html')


def mesero(request):
    return render(request, 'test/vistamesero.html')


def reclamos(request):
    data = {
        'formulario':reclamoForm
    }
    if request.method == 'POST':
        formulario = reclamoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            formulario = reclamoForm()
    return render(request, 'web/vista/reclamos.html', data)

def listarReclamos(request):
    reclamos = Reclamo.objects.all()
    context = {
        'titulo': 'Productos',
        'reclamos': reclamos,
    }
    return render(
        request,
        'web/vista/lista_reclamos.html',
        context
    )

