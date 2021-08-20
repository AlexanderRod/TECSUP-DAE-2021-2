from django.urls import path

from . import views

urlpatterns = [
    # ex: localhost:8080/app/
    path('', views.index, name='index'),

    # ex: localhost:8000/app/sumar/4/5/
    path('sumar/<int:numero1>/<int:numero2>', views.sumar, name='sumar'),

    # ex: localhost:8000/app/restar/4/5/
    path('restar/<int:numero1>/<int:numero2>', views.restar, name='restar'),

    # ex: localhost:8000/app/multiplicar/5/6/
    path('multiplicar/<int:numero1>/<int:numero2>', views.multiplicar, name='multiplicar'),
]
