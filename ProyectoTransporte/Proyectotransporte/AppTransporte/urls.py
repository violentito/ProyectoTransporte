
from django.urls import path, include
from AppTransporte import views

urlpatterns = [
  
    path('inicio/', views.inicio, name="Inicio"),
    path('pasajero/', views.pasajero, name="Pasajero"),
    path('chofer/', views.chofer, name="Chofer"),
    path('transporte/', views.transporte, name="Transporte"),
    path('terminal/', views.terminal, name="Terminal"),
]