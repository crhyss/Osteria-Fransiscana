from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate, hashers
from cliente.forms import direccionForm, userForm,reclamoForm, reservaForm,profileForm,carritoForm,seleccionForm
from cliente.models import Direccion, Region, Reclamo , User, Reserva, Comuna
from django.contrib.auth.forms import AuthenticationForm
from productos.models import Producto, Categoria_prod
from django.core.paginator import Paginator
from web.models import Estado_venta,Carrito,Seleccion 
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
def registro(request):
    if request.user.is_authenticated:
        carrito = Carrito.llamar_carrito(request.user.id_user)
        listar= (Seleccion.objects.filter(id_carrito = carrito.id_carrito).select_related('id_prod')
        .values('id_seleccion','cantidad','id_prod__id_producto','id_prod__prod_nombre','id_prod__prod_imagen','id_prod__prod_precio_of','id_prod__id_producto')) 
    else:
        carrito = None
        listar = None
    data = {
        'formulario': userForm(),
        'carrito':carrito,
        'listar':listar
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
                messages.add_message(request, level=messages.SUCCESS , message="¡Usuario registrado correctamente!")
                return redirect(to='entrar')
            else:
                messages.add_message(request, level=messages.WARNING , message="¡Las contraseñas ingresadas no coinciden!")
                return redirect(to= "loby")
        else:
            messages.add_message(request, level=messages.ERROR , message="¡Usuario ingresado no existe!")
            return redirect(to= "registro")
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
        if request.user.is_authenticated:
            usr = User.objects.get(pk = request.user.id_user)
            usr.user_direccion = datos
    return render(request, 'registration/registroDir.html', data)

def entrar(request):
    if request.method == 'POST':
        #user = User.objects.get(user_correo = request.POST["correo"])
        user = authenticate(request, username = request.POST["correo"], password = request.POST["pass"])
        if user is not None:
            login(request, user)
            messages.add_message(request, level=messages.SUCCESS , message="¡Sesión iniciada correctamente!")
            if user.is_superuser:
                messages.add_message(request, level=messages.SUCCESS , message="¡Sesión iniciada como administrador!")
                return redirect(to="/admin")
            else:
                return redirect(to= "loby")
        else:
            messages.add_message(request, level=messages.WARNING , message="¡Correo o contraseña no son válidos!")
    return render(request, 'registration/login.html')

def salir(request):
    logout(request)
    messages.add_message(request, level=messages.SUCCESS, message="¡Sesión cerrada correctamente!")
    return redirect(to='loby')

def is_valid_queryparam(param):
    return param != '' and param is not None

def carrito(request):
    productos = Producto.objects.all()
    buscar = request.GET.get('buscar')
    lista = Categoria_prod.objects.all()
    if request.user.is_authenticated:
        carrito = Carrito.llamar_carrito(request.user.id_user)
        listar= (Seleccion.objects.filter(id_carrito = carrito.id_carrito).select_related('id_prod')
        .values('id_seleccion','cantidad','id_prod__id_producto','id_prod__prod_nombre','id_prod__prod_imagen','id_prod__prod_precio_of','id_prod__id_producto')) 
    else:
        carrito = None
        listar = None
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
        'carrito':carrito,
        'listar':listar
    }

    return render(request, 'carrito/carta.html',context)

def pedido(request):
    if request.user.is_authenticated:
        carrito = Carrito.llamar_carrito(request.user.id_user)
        listar= (Seleccion.objects.filter(id_carrito = carrito.id_carrito).select_related('id_prod')
        .values('id_seleccion','cantidad','id_prod__id_producto','id_prod__prod_nombre','id_prod__prod_imagen','id_prod__prod_precio_of','id_prod__id_producto')) 
    else:
        carrito = None
        listar = None
    context = {
        'carrito':carrito,
        'listar':listar
    }
    return render(request, 'carrito/pedido.html',context)

def mesero(request):
    return render(request, 'test/vistamesero.html')

def reclamos(request):
    if request.user.is_authenticated:
        carrito = Carrito.llamar_carrito(request.user.id_user)
        listar= (Seleccion.objects.filter(id_carrito = carrito.id_carrito).select_related('id_prod')
        .values('id_seleccion','cantidad','id_prod__id_producto','id_prod__prod_nombre','id_prod__prod_imagen','id_prod__prod_precio_of','id_prod__id_producto')) 
    else:
        carrito = None
        listar = None
    br= request.GET.get('categoria')
    context = {
        'carrito':carrito,
        'listar':listar,
        'formulario':reclamoForm
    }
    if request.method == 'POST':
        formulario = reclamoForm(data=request.POST)
        if formulario.is_valid():
            messages.add_message(request, level=messages.SUCCESS, message="¡Reclamo Ingresado correctamente!")
            formulario.save()
        else:
            formulario = reclamoForm()
    return render(request, 'web/vista/reclamos.html', context)

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
@login_required(login_url='/accounts/login/')
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
@login_required(login_url='/accounts/login/')
def perfilCliente(request):
    usuario = User.objects.all()
    context = {
        'titulo' : 'perfil',
        'usuarios' : usuario
    }
    return render (request,
    'registration/perfilCliente.html',
    context)
@login_required(login_url='/accounts/login/')
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
    if request.user.is_authenticated:
        carrito = Carrito.llamar_carrito(request.user.id_user)
        listar= (Seleccion.objects.filter(id_carrito = carrito.id_carrito).select_related('id_prod').values('id_seleccion','cantidad','id_prod__id_producto','id_prod__prod_nombre','id_prod__prod_imagen','id_prod__prod_precio_of','id_prod__id_producto')) 
    else:
        carrito = None
        listar = None
    if request.method == 'POST':
        formulario = reservaForm(request.POST, instance=usuario)
        if formulario.is_valid():
            reserva = Reserva.buscar_reserva(
                    request.POST["fecha_reserva"],
                    request.POST["hora_reserva"],
                    request.POST["reserva_mesa"]
                )
            hr_valida = Reserva.validar_hora(
                    request.POST["fecha_reserva"],
                    request.POST["hora_reserva"],
                    request.POST["reserva_mesa"]
                )
            if not reserva:
                if hr_valida:
                    Reserva.guardar_reserva(
                    fecha = request.POST["fecha_reserva"],
                    hora = request.POST["hora_reserva"],
                    mesa = request.POST["reserva_mesa"],
                    evento = request.POST["reserva_evento"],
                    usuario = usuario.id_user,
                )
                    messages.add_message(request, level=messages.SUCCESS, message="¡Reserva ingresada correctamente!")
                    return redirect('/')
                else:
                    messages.add_message(request, level=messages.ERROR, message="La mesa seleccionada ya está reservada")
                    return redirect('/logeo/reserva/' + str(usuario.id_user))
            else:
                messages.add_message(request, level=messages.ERROR, message="La mesa ya está reserveda en ese horario")
                return redirect('/logeo/reserva/' + str(usuario.id_user))
    else:
        formulario = reservaForm()
    
    context = {
        'titulo' : 'Reservar Mesa',
        'formulario' : formulario,
        'usuario': usuario,
        'carrito':carrito,
        'listar':listar
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
@login_required(login_url='/accounts/login/')
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
        
def confirmacionDelivery(request,id):
    estado = Estado_venta.objects.get(pk=id)
    context = {
        'estado': estado,

    }
    return render(
        request, 
        'carrito/confirmacion-delivery.html',context
    )    

def orders(request):
    formcart= Carrito.llamar_carrito(request.user.id_user)
    seleccion= Carrito.agregar_prod(request.user.id_user,request.POST["idProd"])
    listar= Carrito.listar_prod(request.user.id_user)
    contar= Seleccion.objects.all().count()
    print(listar)
    context = {
        'formcart':formcart,
        'seleccion':seleccion,
        'listar':listar,
        'contar':contar
        
    }
    return render(
        request, 
        'carrito/carta.html',context
    )
@csrf_exempt
def deletecart(request):
    formcart= Carrito.llamar_carrito(request.user.id_user)
    Carrito.eliminar_prod(formcart.id_carrito,request.POST["idProd"])
    listar= Carrito.listar_prod(request.user.id_user)
    context = {
        'listar':listar,
        'formcart':formcart
    }
    return render(
        request, 
        'carrito/cart.html',context
    )

def addcart(request):
    print(request)
    formcart= Carrito.llamar_carrito(request.user.id_user)
    seleccion= Carrito.agregar_prod(request.user.id_user,request.POST["idProd"])
    listar= Carrito.listar_prod(request.user.id_user)
    context = {
        'listar':listar,
        'formcart':formcart,
        'seleccion':seleccion,
    }
    return render(
        request, 
        'carrito/cart.html',context
    )

def menu(request):
    return render(
        request, 
        'vista/menu.html'
    )