# reportes/views.py
from django.shortcuts import render, redirect
from .models import Personal, Insumo
from agendamiento.models import Cita
from .forms import PersonalForm, InsumoForm

def crear_insumo(request):
    if request.method == 'POST':
        form = InsumoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestion_stock') # Vuelve a la lista de stock
    else:
        form = InsumoForm() # Formulario vacío

    context = {
        'form': form
    }
    return render(request, 'reportes/crear_insumo.html', context)
def dashboard_reportes(request):
    """
    Muestra el menú principal del Módulo 4.
    """
    return render(request, 'reportes/dashboard_reportes.html')

def gestion_personal(request):
    """
    Muestra el listado de personal médico y administrativo.
    """
    personal_lista = Personal.objects.all().order_by('rol', 'nombre_completo')
    
    context = {
        'personal_lista': personal_lista
    }
    return render(request, 'reportes/gestion_personal.html', context)


def gestion_stock(request):
    stock_lista = Insumo.objects.all().order_by('nombre')
    context = {
        'stock_lista': stock_lista
    }
    return render(request, 'reportes/gestion_stock.html', context)

def reporte_atenciones(request):
    citas_completadas = Cita.objects.filter(estado='COMPLETADA')
    
    context = {
        'citas': citas_completadas
    }
    return render(request, 'reportes/reporte_atenciones.html', context)

def reporte_ingresos(request):
    context = {
        'ingreso_total': 1500000 # Valor de ejemplo
    }
    return render(request, 'reportes/reporte_ingresos.html', context)

def crear_personal(request):
    if request.method == 'POST':
        form = PersonalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestion_personal') # Vuelve a la lista
    else:
        form = PersonalForm() # Formulario vacío

    context = {
        'form': form
    }
    return render(request, 'reportes/crear_personal.html', context)