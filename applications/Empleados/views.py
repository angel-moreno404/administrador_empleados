from django.shortcuts import render

from django.views.generic import TemplateView
# Create your views here.


class IndexView(TemplateView):
    template_name = 'empleados/home.html'

class PruebaFundation(TemplateView):
    template_name = 'empleados/fundation_prueba.html'
class Prueba1(TemplateView):
    template_name = 'empleados/prueba1.html'
class Prueba2(TemplateView):
    template_name = 'empleados/prueba2.html'
class Prueba3(TemplateView):
    template_name = 'empleados/prueba3.html'
