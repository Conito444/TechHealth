from django.contrib import admin
from django.urls import path, include
from pacientes import views as pacientes_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pacientes_views.home_view, name='home'),
    path('pacientes/', include('pacientes.urls')), # <-- Módulo 1
    path('agendamiento/', include('agendamiento.urls')), # Módulo 2
    path('clinica/', include('clinica.urls')),      # Módulo 3
    path('reportes/', include('reportes.urls')),  # Módulo 4
]