import requests
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from urllib3.exceptions import InsecureRequestWarning
import urllib3
from .forms import DatosForm, HistorialForm # Import DatosForm from the forms module

# Deshabilitar advertencias de seguridad SSL
urllib3.disable_warnings(InsecureRequestWarning)

def verificacion(request):
    return render(request, 'veraz/verificacion.html')

def index(request):
    return render(request, 'veraz/index.html')

def veraz(request):
    if request.method == 'POST':
        opcion = request.POST.get('opcion')  # Obtener la opción seleccionada
        if opcion == 'A':
            return redirect('deuda_5_anios')  # Redirige a deuda_5_anios
        elif opcion == 'B':
            return redirect('deuda_menos')  # Redirige a deuda_menos
        elif opcion == 'C':
            return redirect('tarjeta_3_anios')  # Redirige a tarjeta_3_anios
        elif opcion == 'D':
            return redirect('tarjeta_menos')  # Redirige a tarjeta_menos
    return render(request, 'veraz/verificacion.html')

def deuda_5_anios(request):
    if request.method == 'POST':
        form = DatosForm(request.POST)
        if not form.is_valid():
            return JsonResponse({'success': False, 'errors': form.errors})
        
        form.save()
        return JsonResponse({'success': True})
    else:
        form = DatosForm()
    return render(request, 'veraz/deuda_5_anios.html', {'form': form})
def deuda_menos(request):
    return render(request, 'veraz/deuda_menos_5_anios_form.html')

def tarjeta_3_anios(request):
    return render(request, 'veraz/deuda_5_anios.html')

def tarjeta_menos(request):
    return render(request, 'veraz/deuda_menos_5_anios_form.html')

def datos_guardados(request):
    return render(request, 'veraz/datos_guardados.html')

def historial_view(request):
    if request.method == 'POST':
        form = HistorialForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            print(form.errors)  # Agregar esto para ver los errores del formulario en la consola del servidor
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = HistorialForm()
    return render(request, 'veraz/historial.html', {'form': form})


def quienes_somos(request):
    return render(request, 'veraz/quienes_somos.html')

@csrf_exempt
def consultar_estado(request):
    if request.method == 'POST':
        cuil = request.POST.get('cuil')
        if not cuil:
            return JsonResponse({"error": "El campo CUIL es obligatorio."}, status=400)

        try:
            print(f"Consultando estado para CUIL: {cuil}")
            url = f'https://api.bcra.gob.ar/CentralDeDeudores/v1.0/Deudas/{cuil}'
            response = requests.get(url, verify=False)
            
            print(f"Respuesta de la API externa: {response.status_code} - {response.text}")
            if response.status_code != 200:
                return JsonResponse({
                    "error": "Error al consultar la API externa.",
                    "status_code": response.status_code,
                    "respuesta": response.text
                }, status=response.status_code)

            data = response.json()
            print(f"Datos recibidos de la API externa: {data}")
            
            identificacion = data['results'].get('identificacion', 'Identificación no especificada')
            denominacion = data['results'].get('denominacion', 'Denominación no especificada')
            periodos = data['results'].get('periodos', [])

            return JsonResponse({
                "identificacion": identificacion,
                "denominacion": denominacion,
                "periodos": periodos
            })
        
        except requests.RequestException as e:
            print(f"Error al conectar con la API externa: {e}")
            return JsonResponse({
                "error": "No se pudo conectar a la API externa.",
                "detalles": str(e)
            }, status=500)

    return JsonResponse({"error": "Método no permitido."}, status=405)

@csrf_exempt
def verificar(request):
    if request.method == 'POST':
        # Lógica para manejar la verificación de supresión de datos
        return JsonResponse({"mensaje": "Verificación realizada con éxito."})
    return JsonResponse({"error": "Método no permitido."}, status=405)