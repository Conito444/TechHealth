# agendamiento/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cita
from pacientes.models import Paciente  # Importamos Paciente
from .forms import CitaForm           # Importamos nuestro nuevo formulario

def crear_cita(request, paciente_id):
    # 1. Obtener el paciente (o mostrar error 404 si no existe)
    paciente = get_object_or_404(Paciente, id=paciente_id)
    
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            # 2. No guardar en la BD todavía
            cita = form.save(commit=False) 
            
            # 3. Asignar el paciente (obtenido de la URL)
            cita.paciente = paciente 
            
            # 4. Ahora sí, guardar la cita completa
            cita.save()
            
            # 5. Redirigir al dashboard principal
            return redirect('dashboard_admin') 
    else:
        # Si es GET (primera visita), mostrar un formulario vacío
        form = CitaForm()

    # 6. Renderizar el template
    context = {
        'form': form,
        'paciente': paciente  # Pasamos el paciente al template para saber para quién es
    }
    return render(request, 'agendamiento/crear_cita.html', context)