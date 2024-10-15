from django.shortcuts import render
from django.views.generic import TemplateView, ListView,CreateView
from django.views.generic.edit import FormView
# Create your views here.
from .models import Prueba, Departamento
from applications.persona.models import Persona
from .forms import PruebaForm, NewDepartament
from django.urls import reverse_lazy 

class IndexView(TemplateView):
    template_name = 'departamento/home.html'

class PruebaListView(ListView):
    template_name = 'departamento/lista.html'
    queryset=['a','b','c']
    context_object_name= 'lista_prueba'

class ModeloTryListView(ListView):
    model = Prueba
    template_name = "departamento/lista_prueba_m.html"
    context_object_name='lista_prueba_m'

    class Meta:
        verbose_name = 'My Departament'
        verbose_name_plural= 'Departaments'
class FormPrueba(CreateView):
    model = Prueba
    template_name = 'departamento/formulario.html'
    form_class= PruebaForm
    success_url = '/'
class NewRegisterDepartament(FormView):
    template_name = 'departamento/newregister.html'
    form_class = NewDepartament
    success_url= reverse_lazy('persona_app:home')


    def form_valid(self, form):

        depa= Departamento(
            name= form.cleaned_data['departamento'],
            short_name= form.cleaned_data['nombre_corto']
        )
        depa.save()
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']
        Persona.objects.create(
            first_name= nombre,
            last_name = apellido,
            job= '1',
            departamento =depa
        )

        return super(NewRegisterDepartament, self).form_valid(form)

class DepartamentoListView(ListView):
    model = Departamento
    template_name='departamento/list.html'
    context_object_name='departamentos'
