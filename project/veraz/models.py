from django.db import models

# Create your models here.
from django.db import models

class Formulario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    numero_gestion = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

from django.db import models

class Datos(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    direccion = models.CharField(max_length=200)
    numero_gestion = models.CharField(max_length=50)
    archivo = models.FileField(upload_to='archivos/', null=True)  # Campo para subir archivos
