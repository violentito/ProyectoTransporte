
from django.urls import path
from AppTransporte import views

urlpatterns = [
  
    path('inicio/', views.inicio, name="Inicio"),
    path('pasajero/', views.pasajero, name="Pasajero"),
    path('chofer/', views.chofer, name="Chofer"),
    path('transporte/', views.transporte, name="Transporte"),
    path('terminal/', views.terminal, name="Terminal"),
    path('pasajeroFormulario', views.pasajeroFormulario),
    path('choferFormulario', views.choferFormulario),
    path('transporteFormulario', views.transporteFormulario),
    path('terminalFormulario', views.terminalFormulario),
    path('login', views.login_request, name="Login"),
    path('register', views.register, name="Register"),
    path('chofer/list', views.ChoferList.as_view(), name='List'),
    path('pasajero/list', views.PasajeroList.as_view(), name='ListP'),
    path('transporte/list', views.TransporteList.as_view(), name='ListT'),

    #URLS TRANSPORTE
    path(r'^/transporte/(?P<pk>\d+)$', views.TransporteDetalle.as_view(), name='DetailT'),
    path(r'^nuevo$', views.TransporteCreacion.as_view(), name='NewT'),
    path(r'^/transporte/editar(?P<pk>\d+)$', views.TransporteUpdate.as_view(), name='EditT'),
    path(r'^/transporte/borrar(?P<pk>\d+)$', views.TransporteDelete.as_view(), name='DeleteT'),

    #URLS PASAJERO
    path(r'^/pasajero/(?P<pk>\d+)/$', views.PasajeroDetalle.as_view(), name='DetailP'),
    path(r'^/pasajero/nuevo/$', views.PasajeroCreacion.as_view(), name='NewP'),
    path(r'^/pasajero/editar(?P<pk>\d+)/$', views.PasajeroUpdate.as_view(), name='EditP'),
    path(r'^/pasajero/borrar(?P<pk>\d+)/$', views.PasajeroDelete.as_view(), name='DeleteP'),
   
    #URLS CHOFER
    path(r'^/chofer/(?P<pk>\d+)$', views.ChoferDetalle.as_view(), name='Detail'),
    path(r'^/chofer/nuevo$', views.ChoferCreacion.as_view(), name='New'),
    path(r'^/chofer/editar(?P<pk>\d+)$', views.ChoferUpdate.as_view(), name='Edit'),
    path(r'^/chofer/borrar(?P<pk>\d+)$', views.ChoferDelete.as_view(), name='Delete'),

    
]