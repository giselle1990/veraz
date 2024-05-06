from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('veraz/', views.verificar_supresion_de_datos, name='veraz'),
]
