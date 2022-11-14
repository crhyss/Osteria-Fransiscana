from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from cliente.forms import direccionForm, userForm,reclamoForm, reservaForm,profileForm
#, direccionForm
from cliente.models import Direccion, Region, Reclamo , Usuario, Reserva
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
    return render(request, 'carrito/carta.html')

def pedido(request):
    return render(request, 'carrito/pedido.html')


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

def reserva(request):
    lista = Reserva.objects.all()
    formulario = None
    if request.method == 'POST':
        formulario = reservaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('/logeo/perfil')
    else:
        formulario = reservaForm()
    context = {
        'titulo' : 'Reservar Mesa',
        'formulario' : formulario,
        'lista' : lista
    }
    return render(
        request, 
        'vista/reserva.html', 
        context
    )