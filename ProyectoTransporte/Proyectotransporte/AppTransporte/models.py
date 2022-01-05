from django.db import models

# Create your models here.


class Pasajero(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    numeroDeDocumento = models.IntegerField()
    vacunado = models.BooleanField()
    def __str__(self):
        return f'Nombre: {self.nombre} Apellido: {self.apellido}'

class Chofer(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    numeroDeDocumento = models.IntegerField()
    numeroDeLicencia = models.IntegerField()
    def __str__(self):
        return f'Apellido: {self.apellido} Numero de documento: {self.numeroDeDocumento}'

class Transporte(models.Model):
    tipo = models.CharField(max_length=40) #Tipo: Aereo o terrestre
    empresa = models.CharField(max_length=40) #Empresa a cargo
    capacidad = models.IntegerField() #Capacidad del transporte
    patente = models.IntegerField()
    def __str__(self):
        return f'Tipo: {self.tipo} Empresa: {self.empresa} Capacidad {self.capacidad} Patente: {self.patente}'

class Terminal(models.Model):
    nombre = models.CharField(max_length=40)
    ubicacion = models.CharField(max_length=40)
    def __str__(self):
        return f'Nombre: {self.nombre} Ubicacion: {self.ubicacion}'


