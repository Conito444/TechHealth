from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_admin, name='dashboard_admin'),
    path('registrar/', views.registrar_paciente, name='registrar_paciente'),
]

