from django.db import models
from django.utils import timezone


class Participante(models.Model):
    nombre = models.CharField(max_length=140, default="")


    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombreproducto = models.CharField(max_length=140, default="")
    cantidad = models.IntegerField(default=0)
    fechavencimiento = models.DateField()

    def __str__(self):
        return self.nombreproducto

class Productosconsumido(models.Model):
    nombre=models.ForeignKey(Participante, on_delete="on_delete")
    nombreproducto=models.ForeignKey(Producto, on_delete="on_delete")
    cantidadconsumida=models.IntegerField(default=0)

    def __str__(self):
        return str(self.cantidadconsumida)