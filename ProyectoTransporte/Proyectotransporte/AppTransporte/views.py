from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse
from django.utils.translation import *
from AppTransporte.models import Chofer, Pasajero, Transporte, Terminal
from AppTransporte.forms import ChoferFormulario, PasajeroFormulario, TransporteFormulario, TerminalFormulario, UserRegisterForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppTransporte/inicio.html" ,  {"mensaje":f"{username} Creado :)"})


      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"AppTransporte/register.html" ,  {"form":form})

def login_request(request):


      if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)

            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')

                  user = authenticate(username=usuario, password=contra)

            
                  if user is not None:
                        login(request, user)
                       
                        return render(request,"AppTransporte/inicio.html",  {"mensaje":f"Bienvenido {usuario}"} )
                  else:
                        
                        return render(request,"AppTransporte/inicio.html", {"mensaje":"Error, datos incorrectos"} )

            else:
                        
                        return render(request,"AppTransporte/inicio.html" ,  {"mensaje":"Error, formulario erroneo"})

      form = AuthenticationForm()

      return render(request,"AppTransporte/login.html", {'form':form} )

## VIEWS TRANSPORTE
class TransporteDelete(DeleteView):

      model = Transporte
      success_url = "AppTransporte/transporte/list"

class TransporteUpdate(UpdateView):

      model = Transporte
      success_url = "AppTransporte/transporte/list"
      fields = ['tipo', 'empresa', 'capacidad', 'patente']


class TransporteCreacion(CreateView):

      model = Transporte
      success_url = "AppTransporte/transporte/list"
      fields = ['tipo', 'empresa', 'capacidad', 'patente']

class TransporteDetalle(DetailView):

      model = Transporte
      template_name = "AppTransporte/transporte_detalle.html"

class TransporteList(ListView):

      model = Transporte
      template_name = "AppTransporte/transporte_list.html"


## VIEWS PASAJERO
class PasajeroDelete(DeleteView):

      model = Pasajero
      success_url = "AppTransporte/pasajero/list"

class PasajeroUpdate(UpdateView):

      model = Pasajero
      success_url = "AppTransporte/pasajero/list"
      fields = ['nombre', 'apellido', 'numeroDeDocumento', 'vacunado']


class PasajeroCreacion(CreateView):

      model = Pasajero
      success_url = "AppTransporte/pasajero/list"
      fields = ['nombre', 'apellido', 'numeroDeDocumento', 'vacunado']

class PasajeroDetalle(DetailView):

      model = Pasajero
      template_name = "AppTransporte/pasajero_detalle.html"

class PasajeroList(ListView):

      model = Pasajero
      template_name = "AppTransporte/pasajero_list.html"

## VIEWS CHOFER
class ChoferDelete(DeleteView):

      model = Chofer
      success_url = "AppTransporte/chofer/list"

class ChoferUpdate(UpdateView):

      model = Chofer
      success_url = "AppTransporte/chofer/list"
      fields = ['nombre', 'apellido', 'numeroDeDocumento', 'numeroDeLicencia']


class ChoferCreacion(CreateView):

      model = Chofer
      success_url = "AppTransporte/chofer/list"
      fields = ['nombre', 'apellido', 'numeroDeDocumento', 'numeroDeLicencia']

class ChoferDetalle(DetailView):

      model = Chofer
      template_name = "AppTransporte/chofer_detalle.html"

class ChoferList(ListView):

      model = Chofer
      template_name = "AppTransporte/chofer_list.html"



def choferFormulario(request):
    
      if request.method == 'POST':

            miFormulario = ChoferFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  chofer = Chofer (nombre=informacion['nombre'], apellido=informacion['apellido'], numeroDeDocumento=informacion['numeroDeDocumento'], numeroDeLicencia=informacion['numeroDeLicencia']) 

                  chofer.save()

                  return render(request, "AppTransporte/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= ChoferFormulario() #Formulario vacio para construir el html

      return render(request, "AppTransporte/choferFormulario.html", {"miFormulario":miFormulario})
  
def pasajeroFormulario(request):
        
      if request.method == 'POST':

            miFormulario = PasajeroFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  pasajero = Pasajero (nombre=informacion['nombre'], apellido=informacion['apellido'], numeroDeDocumento=informacion['numeroDeDocumento'], vacunado=informacion['vacunado']) 

                  pasajero.save()

                  return render(request, "AppTransporte/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= PasajeroFormulario() #Formulario vacio para construir el html
 
      return render(request, "AppTransporte/pasajeroFormulario.html", {"miFormulario":miFormulario})
  
def transporteFormulario(request):
        
      if request.method == 'POST':

            miFormulario = TransporteFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  transporte = Transporte (tipo=informacion['tipo'], empresa=informacion['empresa'], capacidad=informacion['capacidad'], patente=informacion['patente']) 

                  transporte.save()

                  return render(request, "AppTransporte/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= TransporteFormulario() #Formulario vacio para construir el html

      return render(request, "AppTransporte/transporteFormulario.html", {"miFormulario":miFormulario})
  
def terminalFormulario(request):
        
      if request.method == 'POST':

            miFormulario = TerminalFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  terminal = Terminal (nombre=informacion['nombre'], ubicacion=informacion['ubicacion']) 

                  terminal.save()

                  return render(request, "AppTransporte/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= TerminalFormulario() #Formulario vacio para construir el html

      return render(request, "AppTransporte/terminalFormulario.html", {"miFormulario":miFormulario})  




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

