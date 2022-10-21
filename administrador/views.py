from django.shortcuts import render
from django.contrib.auth import models

def administrador(request):
    usuarios = models.User.objects.all()
    grupos = models.Group.objects.all()
    permisos = models.Permission.objects.all()
    context = {
        'titulo': 'Usuario',
        'usuarios': usuarios,
        'grupos':grupos,
        'permisos':permisos,
    }
    return render(request, 'administrador/principal.html',context)