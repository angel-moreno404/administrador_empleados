from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy 
from .models import Persona
# Create your views here.

class ListEmployer(ListView):
    paginate_by = 4
    template_name = 'persona/lista_employers.html'
    def get_queryset(self):
        word=self.request.GET.get("kword",'')
        lista=Persona.objects.filter(
            first_name__icontains=word)
        return lista
    context_object_name = 'empleados'


class ListByArea(ListView):
    template_name= 'persona/personabyarea.html'
    context_object_name='list_area'
    def get_queryset(self):
        search=self.kwargs['short_name']
        lista=Persona.objects.filter(
        departamento__short_name=search)
       
        return lista

class ListByWork(ListView):
    template_name= 'persona/personabywork.html'
    
    def get_queryset(self):
        search=self.kwargs['job']
        lista=Persona.objects.filter(
            job=search)
        return lista
    context_object_name='dates'
    
class SearchByWord(ListView):
    template_name= 'persona/search_by_word.html'
    def get_queryset(self):
        word=self.request.GET.get("kword",'')
        lista=Persona.objects.filter(
            first_name=word)
        return lista
    context_object_name='dates'

class ListHabilidadesEmpleado(ListView):
    template_name='persona/listhabilidad.html'
    context_object_name= 'dates'
    def get_queryset(self):
       empleado=self.request.GET.get("skill",'')
       empleado=Persona.objects.get(id=empleado)
       
       
       return empleado.habilidad.all()


#lista todos los empleados de la empresa. ->
#  lista a todos los empleados que pertenescan a un area de la empresa ->
#  lista empleados por trabajo, -> ->
#  listar empleados por palabra clave->
#  listar habilidad de un empleado->

class EmpleadoDetailView(DetailView):
    model=Persona
    template_name='persona/detail.html'
    context_object_name='empleado'
    def get_context_data(self, **kwargs):

        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)

        context['titulo'] = 'Empleado del mes'
        return context

class SuccessViewp(TemplateView):
    template_name='persona/success.html'

class EmpleadoCreateView(CreateView):
    model=Persona
    template_name='persona/add.html'
    fields=['first_name','last_name','job', 'departamento', 'habilidad', 'hoja_vida', 'avatar',]
    success_url= reverse_lazy('persona_app:manage')

    def form_valid(self,form):
        empleado=form.save(commit=False)
        empleado.full_name = empleado.first_name+' '+empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)

class UpdateEmpleado(UpdateView):

    template_name='persona/update.html'
    model=Persona
    fields=['first_name','last_name','job', 'departamento', 'habilidad', 'avatar',]
    success_url= reverse_lazy('persona_app:manage')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
        
    def form_valid(self,form):
      
        return super(UpdateEmpleado, self).form_valid(form)

class EliminarEmpleado(DeleteView):
    model=Persona
    template_name='persona/delete.html'
    success_url= reverse_lazy('persona_app:manage')
    context_object_name ='empleado'

    #start the applications

class HomeScreen(TemplateView):
    template_name='home.html'

class ListEmployeradmin(ListView):
    paginate_by = 10
    template_name = 'persona/lista_employers_admin.html'
    context_object_name = 'empleados'
    model=Persona
    ordering=['first_name']
    