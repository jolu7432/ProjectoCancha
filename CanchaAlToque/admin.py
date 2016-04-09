from django.contrib import admin

# Register your models here.

from .models import Complejo,Cancha,CaracteristicaChancha,Caracteristicas

admin.site.register(Complejo)
admin.site.register(Cancha)
admin.site.register(CaracteristicaChancha)
admin.site.register(Caracteristicas)