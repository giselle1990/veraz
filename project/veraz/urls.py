from django.urls import path
from . import views
from .views import consultar_estado

urlpatterns = [
    path('', views.index, name='index'),  # Ruta raíz
    path('verificacion/', views.veraz, name='veraz'),
    path('deuda-5-anios/', views.deuda_5_anios, name='deuda_5_anios'),
    path('deuda-menos/', views.deuda_menos, name='deuda_menos'),
    path('tarjeta-3-anios/', views.tarjeta_3_anios, name='tarjeta_3_anios'),
    path('tarjeta-menos/', views.tarjeta_menos, name='tarjeta_menos'),
    path('datos-guardados/', views.datos_guardados, name='datos_guardados'),
    path('historial/', views.historial_view, name='historial'),
    path('quienes_somos/', views.quienes_somos, name='quienes_somos'),
    path('consultar_estado/', consultar_estado, name='consultar_estado'),  # Ruta para consultar estado
    path('verificar/', views.verificar, name='verificar'),  # Ruta para verificar
]