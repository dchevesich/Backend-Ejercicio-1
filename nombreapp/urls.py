from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.plantilla_datos),
    path('mostrar-fecha.html', views.mostrar_fecha),
    path('mostrar-edadfutura.html/<int:edad>/<int:yearfuturo>/',
         views.mostrar_edadfutura),
]
