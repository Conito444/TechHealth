# clinica/models.py
from django.db import models
from agendamiento.models import Cita # Importa la Cita del Módulo 2

class Consulta(models.Model):
    # Usamos OneToOneField para que una cita solo pueda tener UNA consulta asociada
    cita = models.OneToOneField(Cita, on_delete=models.CASCADE, primary_key=True)
    
    # --- Requerimientos del Prototipo ---
    motivo_consulta = models.TextField(blank=True, null=True)
    diagnostico = models.TextField()
    observaciones = models.TextField(blank=True, null=True)
    
    # Para el prototipo, guardaremos esto como texto simple.
    # (Una versión avanzada usaría más modelos)
    receta_medica = models.TextField(blank=True, null=True, help_text="Receta generada")
    examenes_solicitados = models.TextField(blank=True, null=True, help_text="Exámenes solicitados")
    derivacion = models.TextField(blank=True, null=True, help_text="Derivación a especialista")

    def __str__(self):
        return f"Consulta para {self.cita.paciente.nombre_completo} ({self.cita.especialidad})"