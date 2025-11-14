from django import forms
from .models import Personal, Insumo

class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ['nombre_completo', 'rut', 'rol', 'especialidad']
        
        labels = {
            'nombre_completo': 'Nombre Completo',
            'rut': 'RUT (ej: 12345678-9)',
            'rol': 'Rol (Médico, Admin, etc.)',
            'especialidad': 'Especialidad (Solo si es Médico)',
        }

class InsumoForm(forms.ModelForm):
    class Meta:
        model = Insumo
        fields = ['nombre', 'descripcion', 'stock_actual', 'stock_minimo']
        
        labels = {
            'nombre': 'Nombre del Insumo',
            'descripcion': 'Descripción (Opcional)',
            'stock_actual': 'Stock Actual',
            'stock_minimo': 'Stock Mínimo (para alertas)',
        }
        
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }