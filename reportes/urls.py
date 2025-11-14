# reportes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Dashboard principal del Módulo 4
    path('', views.dashboard_reportes, name='dashboard_reportes'),
    
    # URLs para cada gestión
    path('personal/', views.gestion_personal, name='gestion_personal'),
    
    path('personal/crear/', views.crear_personal, name='crear_personal'),

    path('stock/', views.gestion_stock, name='gestion_stock'),
    path('reporte_atenciones/', views.reporte_atenciones, name='reporte_atenciones'),
    path('reporte_ingresos/', views.reporte_ingresos, name='reporte_ingresos'),
    path('stock/crear/', views.crear_insumo, name='crear_insumo'),
]