# clinica/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Esta será la página principal del médico (Listado de atenciones del día)
    path('', views.dashboard_medico, name='dashboard_medico'),
    
    # Esta es la página para rellenar la consulta (Registro de consulta)
    path('atender/<int:cita_id>/', views.iniciar_atencion, name='iniciar_atencion'),
]