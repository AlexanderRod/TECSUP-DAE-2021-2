from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Desde la visa de encuestas!")

def sumar(request, numero1, numero2):
    resultado = numero1 + numero2
    return HttpResponse("La suma de %s" % numero1 + " + %s" % numero2 + " = %s" % resultado)

def restar(request, numero1, numero2):
    resultado = numero1 - numero2
    return HttpResponse("La resta de %s" % numero1 + " - %s" % numero2 + " = %s" % resultado)

def multiplicar(request, numero1, numero2):
    resultado = numero1 * numero2
    return HttpResponse("La multiplicación de %s" % numero1 + " x %s" % numero2 + " = %s" % resultado)
