from django.db import models

# Create your models here.

class Publicacion(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=300)
    fecha = models.DateField(null=True)