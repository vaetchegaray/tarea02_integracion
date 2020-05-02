from django.db import models

# Create your models here.


class Ingrediente(models.Model):
    nombre = models.CharField(("name"), max_length=50)
    descripcion = models.CharField(("description"), max_length=200)


class Hamburguesa(models.Model):
    nombre = models.CharField(("name"), max_length=50)
    precio = models.IntegerField(("price"))
    descripcion = models.CharField(("description"), max_length=200)
    imagen = models.CharField(("img"), max_length=200)
    ingredientes = models.ManyToManyField(
        "Ingrediente", verbose_name=("Lista de ingredientes"), blank=True, related_name="hamburguesas")
