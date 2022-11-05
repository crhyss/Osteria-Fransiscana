from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from cliente.forms import direccionForm, userForm, profileForm
#, direccionForm
from cliente.models import Direccion, Region, Usuario
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

def perfil(request, id_usuario):
    perfilUsuario = profileForm.objects.get(pk=id_usuario) 
    formularioPerfil = None
    if request.method == 'POST':
        formularioPerfil = profileForm(request.POST, instance=perfilUsuario)
        if formularioPerfil.is_valid():
            formularioPerfil.save()
            return redirect('/logeo/perfil/')
    else:
        formularioPerfil = profileForm(instance=perfilUsuario)
    context = {
        'titulo' : 'Perfil Usuario',
        'formulario perfil' : formularioPerfil
    }
    return render(
        request,
        'registration/perfilCliente.html', 
        context
    )

def perfilCliente(request):
    usuario = Usuario.objects.all()
    context = {
        'titulo' : 'perfil',
        'usuarios' : usuario
    }
    return render (request,
    'registration/perfilCliente.html',
    context)

def modificarPerfil(request, id_usuario):
    perfilModificado = Usuario.objects.get(pk=id_usuario)
    formularioPerfil = None
    if request.method == 'POST':
        formularioPerfil = profileForm(request.POST, instance=perfilModificado)
        if formularioPerfil.is_valid():
            formularioPerfil.save()
            return redirect('/logeo/perfil/')
    else:
        formularioPerfil = profileForm(instance=perfilModificado)
    context = {
        'titulo': 'Modificar Perfil',
        'formulario': formularioPerfil
    }
    return render(
        request,
        'registration/modificarPerfil.html',
        context
    )