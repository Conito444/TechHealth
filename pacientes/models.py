from django.db import models

# Create your models here.
class Paciente(models.Model):
    rut = models.CharField(max_length=12, unique=True, help_text="RUT sin puntos y con guión")
    nombre_completo = models.CharField(max_length=255)
    prevision = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_completo} ({self.rut})"