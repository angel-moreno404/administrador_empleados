from django.db import models
from applications.departamento.models import  Departamento
from ckeditor.fields import RichTextField
# Create your models here.

JOB_CHOICES=(('0','CONTADOR'),
            ('1','ADMINISTRADOR'),
            ('2','PROGRAMADOR'),
            ('3','OTRO'))

class Habilidad(models.Model):
    name= models.CharField(max_length=30)
    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural='Skills'
        
    def __str__(self):
        return str(self.id) + '-' + self.name 


class Persona(models.Model):
    first_name = models.CharField('first_name', max_length=50)
    last_name = models.CharField('last_name', max_length=50)
    full_name= models.CharField('full_name', max_length=120, blank=True)
    job=models.CharField('job', max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    habilidad = models.ManyToManyField(Habilidad)
    hoja_vida= RichTextField()
    avatar= models.ImageField(upload_to='empleado', blank=True, null=True)
    
    class Meta:
        verbose_name = 'Empleados Taberu'
        verbose_name_plural= 'People Taberu'
        ordering = ['-first_name']
        


    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name + ' '+ self.job