# agendamiento/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Esta URL capturará el ID del paciente, ej: /agendamiento/crear/5/
    path('crear/<int:paciente_id>/', views.crear_cita, name='crear_cita'),
]