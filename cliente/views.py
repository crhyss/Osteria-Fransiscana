from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, hashers
from cliente.forms import direccionForm, userForm,reclamoForm, reservaForm,profileForm
from cliente.models import Direccion, Region, Reclamo , User, Reserva, Comuna
from django.contrib.auth.forms import AuthenticationForm
from productos.models import Producto, Categoria_prod
from django.core.paginator import Paginator


def registro(request):
    data = {
        'formulario': userForm()
    }
    if request.method == 'POST':
        formulario = userForm(data=request.POST)
        if formulario.is_valid():
            if request.POST["password1"] and request.POST["password2"]:
                formulario.Meta.model.objects.create_user(
                    formulario.cleaned_data["user_correo"],
                    formulario.cleaned_data["user_nombre"],
                    formulario.cleaned_data["user_apellidos"],
                    request.POST["password1"]
                )
<<<<<<< HEAD
                message = "{0} {1} su usuario ha sido creado exitosamente".format(formulario.cleaned_data["user_correo"], formulario.cleaned_data["user_apellidos"])
                messages.add_message(request, level=messages.SUCCESS , message="¡Usuario registrado correctamente!")
=======
                mesage = "{0} {1} su usuario ha sido creado exitosamente".format(formulario.cleaned_data["user_correo"], formulario.cleaned_data["user_apellidos"])
                messages.success(request, mesage)
>>>>>>> 66563a0df841e7c93736117d232ff02373d9c67f
                return redirect(to='entrar')
            else:
                messages.add_message(request, level=messages.WARNING , message="¡Las contraseñas ingresadas no coinciden!")
    return render(request, 'registration/registro.html', data)

def addDirec(request):
    data = {
        'formulario': direccionForm,
        'regiones': Region.objects.all(),
        'comunas': Comuna.objects.all()
    }
    if request.method == 'POST':
        formulario = direccionForm(data=request.POST)
        if formulario.is_valid():
            datos = formulario.save(commit=False)
            datos.dir_comuna = Comuna.objects.get(id_comuna = request.POST["comuna"])
            datos.dir_calle = request.POST["dir_calle"].upper()
            if request.POST["dir_depto_nro"] != "":
                datos.dir_depto = True
            datos.save()
            
    return render(request, 'registration/registroDir.html', data)

def entrar(request):
    if request.method == 'POST':
        #user = User.objects.get(user_correo = request.POST["correo"])
        user = authenticate(request, username = request.POST["correo"], password = request.POST["pass"])
        if user is not None:
            login(request, user)
            messages.add_message(request, level=messages.SUCCESS , message="¡Sesión iniciada correctamente!")
            if user.is_superuser:
                return redirect(to="/admin")
            else:
                return redirect(to= "loby")
        else:
<<<<<<< HEAD
            messages.add_message(request, level=messages.WARNING , message="¡Usuario ingresado, no Existe!")
            return redirect(to="registro")
=======
            messages.error(request, "El usuario o contraseña invalidos")
>>>>>>> 66563a0df841e7c93736117d232ff02373d9c67f
    return render(request, 'registration/login.html')

def salir(request):
    logout(request)
    messages.add_message(request, level=messages.SUCCESS, message="¡Sesión cerrada correctamente!")
    return redirect(to='loby')

def is_valid_queryparam(param):
    return param != '' and param is not None

def carrito(request):
    productos = Producto.objects.all()
    qr = Producto.objects.all()
    buscar = request.GET.get('buscar')
    lista = Categoria_prod.objects.all()
    br= request.GET.get('categoria')
    if is_valid_queryparam(buscar):
        productos = productos.filter(prod_nombre__icontains=buscar)
    if is_valid_queryparam(br) and br != 'Categoria':
        productos = productos.filter(prod_categoria__in = br)
    paginator = Paginator(productos, 6)
    page = request.GET.get('page')
    productos = paginator.get_page(page)
    context = {
        'productos': productos,
        'lista': lista,
    }

    return render(request, 'carrito/carta.html',context)

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
            messages.add_message(request, level=messages.SUCCESS, message="¡Reclamo Ingresado correctamente!")
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
    usuario = User.objects.all()
    context = {
        'titulo' : 'perfil',
        'usuarios' : usuario
    }
    return render (request,
    'registration/perfilCliente.html',
    context)

def modificarPerfil(request, id_usuario):
    perfilModificado = User.objects.get(pk=id_usuario)
    formularioPerfil = None
    if request.method == 'POST':
        try:
            formularioPerfil = profileForm(request.POST, instance=perfilModificado)
            if formularioPerfil.is_valid():
                formularioPerfil.save()
                messages.add_message(request, level=messages.SUCCESS, message="¡Perfil modificado exitosamente!")
                return redirect('/logeo/perfil/')
        except:
            messages.add_message(request, level=messages.ERROR, message="¡Error, al modificar los datos!")
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

def reserva(request, id_usuario):
    usuario = User.objects.get(pk=id_usuario) 
    if request.method == 'POST':
        formulario = reservaForm(request.POST, instance=usuario)
        if formulario.is_valid():
            Reserva.guardar_reserva(
                fecha_reserva = request.POST["fecha_reserva"],
                hora_reserva = request.POST["hora_reserva"],
                reserva_mesa = request.POST["reserva_mesa"],
<<<<<<< HEAD
                reserva_evento = request.POST["reserva_evento"],
                reserva_usuario = usuario.id_user,
=======
                reserva_usuario = usuario.id_user
>>>>>>> 66563a0df841e7c93736117d232ff02373d9c67f
            )
            print("fulario")
            messages.add_message(request, level=messages.SUCCESS, message="¡Reserva ingresada correctamente!")
            return redirect('/')
            # return redirect('/logeo/reserva/' + str(id_usuario))
        else:
            messages.add_message(request, level=messages.SUCCESS, message="¡Reserva ingresada correctamente!")
    else:
        formulario = reservaForm()
    context = {
        'titulo' : 'Reservar Mesa',
        'formulario' : formulario,
        'usuario': usuario
    }
    return render(
        request, 
        'vista/reserva.html', 
        context
    )

def historialReservas(request, id_usuario):
    data = {
        'reservas' : Reserva.objects.filter(reserva_usuario = id_usuario)
    }
    return render(
        request, 
        'vista/historialReservas.html',
        data
)

def cambiarContraseña(request, id_usuario):
    usuario = User.objects.get(pk=id_usuario)
    if request.method == 'POST': 
        if hashers.check_password(request.POST["oldpass"], usuario.password):
            try:
                if request.POST["password1"] and request.POST["password2"]:
                    usuario.set_password(request.POST["password1"])
                    usuario.save()
                    messages.add_message(request, level=messages.SUCCESS, message="¡Contraseña modificada correctamente!")
                    return redirect('/logeo/perfil/')
                else:
                    messages.add_message(request, level=messages.ERROR, message="¡Error, al modificar contraseña!")
            except:
                messages.add_message(request, level=messages.ERROR, message="¡Error, al modificar contraseña!")
    return render(request, 'vista/cambiarContraseña.html')  
        


            
