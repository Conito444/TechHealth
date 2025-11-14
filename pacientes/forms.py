from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['rut', 'nombre_completo', 'prevision']
        
        labels = {
            'rut': 'RUT (ej: 12345678-9)',
            'nombre_completo': 'Nombre Completo',
            'prevision': 'Sistema de Previsión',
        }