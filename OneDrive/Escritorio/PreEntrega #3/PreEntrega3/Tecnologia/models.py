from django.db import models

# Create your models here.

class Computadores(models.Model):
    Tipo = models.CharField(max_length=10)
    Marca = models.CharField(max_length=10)
    Modelo = models.CharField(max_length=20)
    Uso = models.BooleanField(default=False)

    def __str__(self):
        return self.Marca

class Telefonos(models.Model):
    Marca = models.CharField(max_length=10)
    Modelo = models.CharField(max_length=20)
    Uso = models.BooleanField(default=False)

    def __str__(self):
        return self.Marca + "" + self.Modelo

class Televisores(models.Model):
    Tipo = models.CharField(max_length=10)
    Marca = models.CharField(max_length=10)
    Modelo = models.CharField(max_length=20)
    Uso = models.BooleanField(default=False)

    def __str__(self):
        return self.Marca + "" + self.Modelo
