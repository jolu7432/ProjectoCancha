from __future__ import unicode_literals

from django.db import models

class Complejo(models.Model):
    """clase Complejo"""
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=250)
    #zona = model.ForeignKey(Zona)
    #localidad = model.ForeignKey(Localidad)
    #provincia = model.ForeignKey(Provincia)

    def __str__(self):
        return self.nombre

class Cancha(models.Model):
    """clase Cancha"""
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

