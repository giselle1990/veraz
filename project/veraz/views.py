from django.shortcuts import render, redirect
from .forms import FormularioForm, DatosForm
from .models import Formulario
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

def index(request):
    if request.method == 'POST':
        form = FormularioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            numero_gestion = generar_numero_gestion()
            return render(request, 'veraz/index.html', {'exito': True, 'numero_gestion': numero_gestion})
    else:
        form = FormularioForm()
    
    return render(request, 'veraz/index.html', {'form': form})

def verificar_supresion_de_datos(request):
    if request.method == 'POST':
        form = DatosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            numero_gestion = generar_numero_gestion()
            logger.debug("Procesamiento exitoso del formulario DatosForm.")
            return render(request, 'veraz/formulario.html', {'exito': True, 'numero_gestion': numero_gestion})
    else:
        form = DatosForm()
    
    return render(request, 'veraz/formulario.html', {'form': form})

def generar_numero_gestion():
    fecha_actual = datetime.now()
    contador = Formulario.objects.count() + 1
    return f"{fecha_actual.strftime('%Y%m%d%H%M%S')}-{contador}"
