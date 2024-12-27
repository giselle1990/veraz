from django.db import models

class Datos(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cuil = models.CharField(max_length=11, default='12345678')
    telefono = models.CharField(max_length=20, default='0000000000')
    email = models.EmailField(max_length=100, default='example@example.com')

    def __str__(self):
        return f'Datos de {self.nombre} {self.apellido}'
    
class Datos_Historial(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=8, default='12345678')  # Agregar campo DNI
    cuil = models.CharField(max_length=11, default='12345678')
    telefono = models.CharField(max_length=20, default='0000000000')
    email = models.EmailField(max_length=100, default='example@example.com')
    detalles_deudas = models.TextField(default='')  # Agregar campo detalles de deudas

    def __str__(self):
        return f'Datos de {self.nombre} {self.apellido}'