# clinica/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone # Para filtrar por la fecha de "hoy"
from agendamiento.models import Cita
from .models import Consulta
from .forms import ConsultaForm

def dashboard_medico(request):
    """
    Muestra el listado de atenciones del día.
    """
    # Obtenemos la fecha de hoy
    hoy = timezone.now().date()
    
    # Filtramos las citas para hoy que estén 'AGENDADA'
    citas_pendientes = Cita.objects.filter(
        fecha_hora__date=hoy,
        estado='AGENDADA'
    ).order_by('fecha_hora') # Ordenar por hora

    # Filtramos las citas para hoy que ya estén 'COMPLETADA'
    citas_completadas = Cita.objects.filter(
        fecha_hora__date=hoy,
        estado='COMPLETADA'
    ).order_by('-fecha_hora') # Ordenar por hora (descendente)

    context = {
        'citas_pendientes': citas_pendientes,
        'citas_completadas': citas_completadas,
        'fecha_hoy': hoy,
    }
    return render(request, 'clinica/dashboard_medico.html', context)


def iniciar_atencion(request, cita_id):
    """
    Maneja el registro de la consulta médica (diagnóstico, recetas, etc.)
    """
    cita = get_object_or_404(Cita, id=cita_id)
    
    # Usamos get_or_create:
    # 1. Intenta obtener la Consulta si ya existe para esta Cita.
    # 2. Si no existe, crea una nueva instancia de Consulta ligada a esta Cita.
    consulta, created = Consulta.objects.get_or_create(cita=cita)

    if request.method == 'POST':
        # Pasamos 'instance=consulta' para actualizar el registro existente
        form = ConsultaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save() # Guarda los datos de la consulta
            
            # Actualizamos el estado de la Cita a 'COMPLETADA'
            cita.estado = 'COMPLETADA'
            cita.save()
            
            # Redirigimos de vuelta al dashboard del médico
            return redirect('dashboard_medico')
    else:
        # Si es GET, mostramos el formulario con los datos existentes (si los hay)
        form = ConsultaForm(instance=consulta)

    context = {
        'form': form,
        'cita': cita,
        'paciente': cita.paciente, # Pasamos el paciente para mostrar sus datos
    }
    return render(request, 'clinica/iniciar_atencion.html', context)