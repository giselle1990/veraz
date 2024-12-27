from django import forms
from .models import Datos, Datos_Historial

class DatosForm(forms.ModelForm):
    class Meta:
        model = Datos
        fields = ['nombre', 'apellido', 'cuil', 'telefono', 'email']
        
        
from django import forms
from .models import Datos_Historial

class HistorialForm(forms.ModelForm):
    class Meta:
        model = Datos_Historial
        fields = ['nombre', 'apellido', 'dni', 'cuil', 'telefono', 'email', 'detalles_deudas']