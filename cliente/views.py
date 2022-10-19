from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from cliente.forms import inicioForm, direccionForm
from cliente.models import Direccion
from django.contrib.auth.forms import AuthenticationForm
import json


def registro(request):
    data = {
        'formulario': inicioForm()
    }
    if request.method == 'POST':
        formulario = inicioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(
                username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            print("Felicidades")
            messages.success(request, "registrado")
            return redirect(to='loby')
        data["formulario"] = formulario
    return render(request, 'registration/registro.html', data)


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
