# reportes/models.py
from django.db import models

class Personal(models.Model):
    """
    Modelo para la Gestión de personal (listado de médicos y administrativos)
    """
    ROL_CHOICES = [
        ('MEDICO', 'Médico'),
        ('ADMIN', 'Administrativo'),
        ('GERENCIA', 'Gerencia'),
    ]
    
    nombre_completo = models.CharField(max_length=255)
    rut = models.CharField(max_length=12, unique=True)
    rol = models.CharField(max_length=10, choices=ROL_CHOICES)
    especialidad = models.CharField(max_length=100, blank=True, null=True, help_text="Solo si el rol es Médico")

    def __str__(self):
        return f"{self.nombre_completo} ({self.get_rol_display()})"

class Insumo(models.Model):
    """
    Modelo para la Gestión básica de stock de insumos médicos
    """
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    stock_actual = models.PositiveIntegerField(default=0)
    stock_minimo = models.PositiveIntegerField(default=10, help_text="Stock mínimo para alertas")

    def __str__(self):
        return f"{self.nombre} (Stock: {self.stock_actual})"