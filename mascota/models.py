from django.db import models

# Create your models here.

class mascotas(models.Model):
    nombre= models.CharField(max_length=255)
    raza = models.CharField(max_length=200)
    edad = models.IntegerField()
    altura = models.FloatField()
    estaVacunado = models.BooleanField(default=False)
