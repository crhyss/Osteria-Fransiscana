from email.policy import default
from pickle import TRUE
from unittest.util import _MAX_LENGTH
from django.db import models

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


class Direccion(Comuna):
    codigo_postal = models.IntegerField(primary_key = True)
    dir_calle = models.CharField(max_length = 50, blank=True)
    dir_nro = models.IntegerField(blank=True)
    dir_depto = models.BooleanField(blank=True)
    dir_depto_nro = models.IntegerField(blank=True,default=None,null=True)
    


class Local(models.Model):
    id_local = models.AutoField(primary_key = True)
    local_activo = models.BooleanField(default=True)
    local_hora_aper = models.DateTimeField(blank = False)
    local_hora_cierr = models.DateTimeField(blank = False)
    local_fono = models.IntegerField(blank = False)
    locar_direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, default=None)

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    usr_nombre = models.CharField(max_length=40, blank=False)
    usr_apellido_pat = models.CharField(max_length=40, blank=False)
    usr_apellido_mat = models.CharField(max_length=40, blank=False)
    usr_pass = models.CharField(max_length=40, blank=False)
    usr_correo = models.EmailField(max_length=100, blank=False)
    usr_activo = models.BooleanField(default=True)
    usr_tipo = models.ForeignKey(Tipo_usuario, on_delete=models.CASCADE, default=3)
    usr_direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, default=None)
