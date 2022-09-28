from django.http import HttpResponse
from django.shortcuts import render, redirect

def paginaprincipal(request):
    return render(
        request,
        'vista/Principal.html'
    )

def login(request):
    return render(
        request,
        'vista/inicio.html'
    )