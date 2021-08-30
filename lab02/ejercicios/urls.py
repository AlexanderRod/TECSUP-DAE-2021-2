from django.urls import path

from . import views

app_name = 'ejercicios'

urlpatterns = [
    # /ejercicios1/
    path('operaciones', views.operaciones, name='operaciones'),
    path('respuesta1',views.calcular,name="respuesta1"),

    # /ejercicios2/
    path('formulario2',views.formulario,name='formulario2'),
    path('resultado',views.calcula,name="resultado"),

]