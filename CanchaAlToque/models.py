from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Complejo(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=250)
    zona = models.ForeignKey(Zona)
    localidad = models.ForeignKey(Localidad)
    provincia = models.ForeignKey(Provincia)

    def __str__(self):
        return self.nombre

class Cancha(models.Model):
    nombre = models.CharField(max_length=200)
    esCubierto = models.BooleanField()
    cantidad = models.IntegerField()

    def __str__(self):
        return self.nombre

class CaracteristicaChancha(models.Model):
    cancha = models.ForeignKey(Cancha)
    caracteristica = models.ForeignKey(Caracteristicas)


class Caracteristicas(models.Model):
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre

class Usuario(User):
    esCapitan = models.BooleanField()
    def __str__(self):
        return self.nombre

class Zona(models.Model):
    nombre = models.CharField(max_length=200)

class Localidad(models.Model):
    nombre = models.CharField(max_length=200)
    cp = models.IntegerField()

class Provincia(models.Model):
    nombre = models.CharField(max_length=200)


class Turno(models.Model):
    cancha = models.ForeignKey(Cancha)
    comienzo = models.DateTimeField()
    fin = models.DateTimeField()
    esActivo = models.BooleanField()
    esCancelado = models.BooleanField()
    esPerdido = models.BooleanField()
    esFijo = models.BooleanField()
    senia = models.ForeignKey(Senia)

class Senia(models.Model):
    monto = models.FloatField()
    vencimiento = models.DateTimeField()

