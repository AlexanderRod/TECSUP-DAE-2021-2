from django.shortcuts import render
import math
# Create your views here.
def operaciones(request):
    context = {
        'titulo': "Operaciones",
    }
    return render(request,'ejercicio1/operaciones.html', context)

def calcular(request):

    a = request.POST['n1']
    b = request.POST['n2']
    suma = int(a) + int(b)
    resta = int(a) - int(b)
    multiplicacion = int(a) * int(b)

    context = {
        'a' : a,
        'b' : b,
        'resultado1' : suma,
        'resultado2' : resta,
        'resultado3' : multiplicacion,
    }

    return render(request,'ejercicio1/respuesta1.html', context)


# Create your views here.
def formulario(request):
    context = {
        'titulo': "formulario",
    }
    return render(request,'ejercicio2/formulario2.html', context)

def calcula(request):

    d = request.POST['n1'] #diametro
    a = request.POST['n2'] #altura
    r = (float(d) / 2) #radio
    volC = (math.pi * (float(a) * float(r)**2 ) )

    context = {
        'diametro': d,
        'altura' : a,
        'radio' : r,
        'resultado1' : volC,
        }
    return render(request,'ejercicio2/resultado.html', context)