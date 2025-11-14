from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente
from .forms import PacienteForm

# Create your views here.

def home_view(request):
    """
    Muestra el menú principal de navegación.
    """
    return render(request, 'home.html')

def dashboard_admin(request):
    context = {} # Un diccionario para pasar datos al HTML

    if request.method == 'POST':
        rut_buscado = request.POST.get('rut-busqueda', None)
        
        if rut_buscado:
            try:
                paciente = Paciente.objects.get(rut=rut_buscado)
                context['paciente_encontrado'] = paciente
            except Paciente.DoesNotExist:
                context['error'] = f"No se encontró ningún paciente con el RUT {rut_buscado}."

    return render(request, 'pacientes/dashboard_admin.html', context)

def registrar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('dashboard_admin')
    
    else:
        form = PacienteForm()

    return render(request, 'pacientes/registrar_paciente.html', {'form': form})