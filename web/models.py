from django.db import models

# Create your models here.

class Tipo_usuario(models.Model):
    id_tipo_usr = models.AutoField(primary_key=True)
    tipo_usr = models.CharField(max_length=40)

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    usr_nombre = models.CharField(max_length=40, blank=False)
    usr_apellido_pat = models.CharField(max_length=40, blank=False)
    usr_apellido_mat = models.CharField(max_length=40, blank=False)
    usr_pass = models.CharField(max_length=40, blank=False)
    usr_correo = models.CharField(max_length=100, blank=False)
    usr_activo = models.BooleanField(default=True)
    usr_tipo = models.ForeignKey(Tipo_usuario, on_delete=models.CASCADE, default=None)