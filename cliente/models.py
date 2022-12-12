from email.policy import default
from pickle import TRUE
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from unittest.util import _MAX_LENGTH
from django.db import models
import datetime
import time

class Region(models.Model):
    id_region = models.AutoField(primary_key = True)
    region_nombre = models.CharField(max_length = 40, blank = False)
    def __str__(self):
        return self.region_nombre
    
class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key = True)
    comuna_nombre = models.CharField(max_length = 40, blank = False)
    comuna_region = models.ForeignKey(Region, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return self.comuna_nombre

class Tipo_usuario(models.Model):
    id_tipo_usr = models.AutoField(primary_key=True)
    tipo_usr = models.CharField(max_length=40)
    def __str__(self):
        return self.tipo_usr


class Direccion(models.Model):
    id_direccion = models.AutoField(primary_key = True)
    dir_calle = models.CharField(max_length = 50, blank = False)
    dir_nro = models.IntegerField(blank = False)
    dir_depto = models.BooleanField(default = False)
    dir_depto_nro = models.IntegerField(blank =True, null = True)
    dir_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return self.dir_calle
    def agregar_dir(dir_calle, dir_nro, dir_depto_nro, comuna):
        if dir_depto_nro == "":
            dir_depto_nro = 0
        try:
            dir = Direccion.objects.get(
                dir_calle = dir_calle,
                dir_nro = dir_nro,
                dir_depto_nro = dir_depto_nro,
                dir_comuna = comuna
            )
            return dir
        except:
            dir = Direccion()
            dir.dir_calle = dir_calle
            dir.dir_nro = dir_nro
            if dir_depto_nro != "":
                dir.dir_depto = True
                dir.dir_depto_nro = dir_depto_nro
            dir.dir_comuna = Comuna.objects.get(id_comuna = comuna)
            dir.save()
            return dir



class Local(models.Model):
    id_local = models.AutoField(primary_key = True)
    local_hora_aper = models.TimeField(blank = False)
    local_hora_cierr = models.TimeField(blank = False)
    local_fono = models.IntegerField(blank = False)
    local_activo = models.BooleanField(default=True)
    local_direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, default=None)
    def __str__(self) -> str:
        return self.locar_direccion

class UserManager(BaseUserManager):
    def _create_user(self, user_correo, user_nombre, user_apellidos, user_tipo, is_superuser, is_staff, user_pass):
        usuario = self.model(
            user_correo = user_correo,
            user_nombre = user_nombre,
            user_apellidos = user_apellidos,
            user_tipo = user_tipo,
            is_superuser = is_superuser,
            is_staff = is_staff
        )
        usuario.set_password(user_pass)
        usuario.save(using = self.db)
        return usuario
    def create_user(self, user_correo, user_nombre, user_apellidos, user_pass):
        usuario = self._create_user(
            user_correo,
            user_nombre,
            user_apellidos,
            Tipo_usuario.objects.get(id_tipo_usr = 1), 
            False,
            False,
            user_pass
        )
    
    def create_superuser(self, user_correo, user_nombre, user_apellidos, user_tipo, user_pass):
        usuario = self._create_user(
            user_correo,
            user_nombre,
            user_apellidos,
            user_tipo,
            True,
            True,
            user_pass
        )

class User(AbstractBaseUser):
    id_user = models.AutoField(primary_key=True)
    user_correo = models.EmailField('Correo Electrónico',max_length=50, unique=True)
    user_nombre = models.CharField(max_length=40)
    user_apellidos = models.CharField(max_length=40)
    user_tipo = models.ForeignKey(Tipo_usuario, on_delete=models.CASCADE)
    user_direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, null=True, blank= True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = UserManager()

    def has_perm(self, perm, obj = None):
        return True

    def has_module_perms(self, app_label):
        return True

    USERNAME_FIELD = "user_correo"
    REQUIRED_FIELDS = ['user_nombre', 'user_apellidos']
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'


class Reclamo(models.Model):
    id_reclamos = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40, blank=False,null=True)
    apellido = models.CharField(max_length=40, blank=False,null=True)
    reclamo_fecha = models.DateTimeField(blank=True, null=True, default=(datetime.datetime.now()))
    reclamo_descrip = models.TextField(max_length=255, blank=False)

class EstadoMesa(models.Model):
    id_estado_mesa = models.AutoField(primary_key=True)
    estado_mesa = models.CharField(max_length=40)
    
    def __str__(self) -> str:
        return self.estado_mesa

class Mesa(models.Model):
    id_mesa = models.AutoField(primary_key=True)
    mesa_nro = models.IntegerField(blank=False)
    mesa_sillas = models.IntegerField(blank=False)
    mesa_estado = models.ForeignKey(EstadoMesa, on_delete=models.CASCADE, default=None)
    mesa_local = models.ForeignKey(Local, on_delete=models.CASCADE, default=1)

    def mesa_limpia(self):
        estado = EstadoMesa.objects.get(id_estado_mesa = 1)
        self.mesa_estado = estado
        self.save() 

    def visualizar_reserva(mesas):
        estado_reservado = EstadoMesa.objects.get(id_estado_mesa = 4)
        estado_libre = EstadoMesa.objects.get(id_estado_mesa = 1)
        fecha_actual = datetime.datetime.now().date()
        hora_actual = datetime.datetime.now().time()
        hora_actual = ("{0}:{1}".format(hora_actual.hour, hora_actual.minute))
        for mesa in mesas:
            print(mesa)
            if not Reserva.validar_hora(fecha_actual, hora_actual, mesa.id_mesa):
                mesa.mesa_estado = estado_reservado
                mesa.save()
        mesas_reserv = Mesa.objects.filter(mesa_estado = 4)
        for mesa in mesas_reserv:
            if Reserva.validar_hora(fecha_actual, hora_actual, mesa.id_mesa):
                mesa.mesa_estado = estado_libre
                mesa.save()

    def __str__(self):
        return str(self.id_mesa)

class Evento(models.Model):
    id_evento = models.AutoField(primary_key=True)
    nombre_evento = models.CharField(max_length=40, blank=False,null=True)
    def __str__(self):
        return str(self.nombre_evento)

class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    fecha_reserva = models.DateField(max_length=40, blank=False)
    hora_reserva = models.TimeField(blank=True, null=True)
    reserva_mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE, default=None)
    reserva_usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    reserva_evento = models.ForeignKey(Evento, on_delete=models.CASCADE, default=None)
    def __str__ (self):
        return str(self.reserva_mesa)

    def guardar_reserva(fecha, hora, mesa, usuario, evento):    
        reserva = Reserva()
        reserva.fecha_reserva = fecha
        reserva.hora_reserva = hora
        reserva.reserva_mesa = Mesa.objects.get(id_mesa = mesa)
        reserva.reserva_usuario = User.objects.get(id_user = usuario)
        reserva.reserva_evento = Evento.objects.get(id_evento = evento)
        reserva.save()
    
    def buscar_reserva(fecha, hora, mesa):
        try:
            reserva = Reserva.objects.get(fecha_reserva = fecha,
                        hora_reserva = hora,
                        reserva_mesa = Mesa.objects.get(id_mesa = mesa)
                    )
            return True
        except:
            return False
    def validar_hora(fecha, hora, mesa):
        try:
            lista = Reserva.objects.filter(fecha_reserva = fecha, reserva_mesa = Mesa.objects.get(id_mesa = mesa))
            for res in lista:
                reserva = datetime.timedelta(hours = res.hora_reserva.hour, minutes= res.hora_reserva.minute)
                nueva_res = time.strptime(hora, "%H:%M")
                nueva_res = datetime.timedelta(hours = nueva_res.tm_hour, minutes= nueva_res.tm_min)
                hr_inicio = reserva - datetime.timedelta(minutes=45)
                hr_final = reserva + datetime.timedelta(minutes=45)
                if nueva_res > hr_inicio and nueva_res < hr_final:
                    return False
            return True
        except:
            print("oh no fallé")
            return True           