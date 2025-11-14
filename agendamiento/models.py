from django.db import models
from pacientes.models import Paciente
# Create your models here.
class Cita(models.Model):
    # --- Requerimientos del Prototipo ---
    centro_medico = models.CharField(max_length=200, default='Centro Principal')
    especialidad = models.CharField(max_length=200)
    
    fecha_hora = models.DateTimeField()

    # --- Conexiones ---
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name="citas")
    
    # --- Estado de la Cita ---
    ESTADO_CHOICES = [
        ('AGENDADA', 'Agendada'),
        ('CANCELADA', 'Cancelada'),
        ('COMPLETADA', 'Completada'),
    ]
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='AGENDADA')

    def __str__(self):
        # Esto ayuda a verla bien en el panel de admin
        return f"Cita de {self.paciente.nombre_completo} ({self.especialidad}) el {self.fecha_hora.strftime('%Y-%m-%d %H:%M')}"