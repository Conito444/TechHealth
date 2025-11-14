# agendamiento/forms.py
from django import forms
from .models import Cita

class CitaForm(forms.ModelForm):

    # Hacemos que la fecha/hora use el widget de calendario del navegador
    fecha_hora = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={'type': 'datetime-local'},
            format='%Y-%m-%dT%H:%M'
        ),
        input_formats=['%Y-%m-%dT%H:%M']
    )

    class Meta:
        model = Cita
        # Solo los campos que el usuario debe rellenar
        fields = ['centro_medico', 'especialidad', 'fecha_hora']

        labels = {
            'centro_medico': 'Centro Médico',
            'especialidad': 'Especialidad',
            'fecha_hora': 'Fecha y Hora de la Cita',
        }