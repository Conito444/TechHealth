# clinica/forms.py
from django import forms
from .models import Consulta

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        exclude = ('cita',) 
        
        widgets = {
            'motivo_consulta': forms.Textarea(attrs={'rows': 3}),
            'diagnostico': forms.Textarea(attrs={'rows': 4}),
            'observaciones': forms.Textarea(attrs={'rows': 4}),
            'receta_medica': forms.Textarea(attrs={'rows': 5}),
            'examenes_solicitados': forms.Textarea(attrs={'rows': 3}),
            'derivacion': forms.Textarea(attrs={'rows': 3}),
        }