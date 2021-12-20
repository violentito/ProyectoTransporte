from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, "AppTransporte/inicio.html")
    
def pasajero(request):
    return render(request, "AppTransporte/pasajero.html")

def chofer(request):
    return render(request, "AppTransporte/chofer.html")

def transporte(request):
    return render(request, "AppTransporte/transporte.html")

def terminal(request):
    return render(request, "AppTransporte/terminal.html")

