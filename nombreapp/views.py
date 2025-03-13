from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.


def plantilla_datos(request):
    return render(request, 'mostrar_plantilla.html')


def mostrar_fecha(request):
    fecha = datetime.now()
    return render(request, 'mostrar-fecha.html', {'fecha': fecha})


def mostrar_edadfutura(request, edad, yearfuturo):
    fecha = datetime.now()
    años_a_sumar = yearfuturo - fecha.year
    edad_futura = edad + años_a_sumar
    return render(request, 'mostrar-edadfutura.html', {"fecha": fecha, "edad_futura": edad_futura, "yearfuturo": yearfuturo})
