from django.db import models


# Create your models here.
class Jugador(models.Model):
    nombre = models.CharField(max_length=50, default=None)
    carta = models.CharField(max_length=200)
    puntaje = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre 

class Repartidor(models.Model):
    nombre = models.CharField(max_length=50, default=None)
    carta = models.CharField(max_length=200)
    puntaje = models.IntegerField(default=0)