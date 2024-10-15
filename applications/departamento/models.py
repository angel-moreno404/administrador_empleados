from django.db import models

# Create your models here.

class Prueba(models.Model):
    title = models.CharField(max_length=30)
    subtitle = models.CharField(max_length=30)
    cantidad= models.IntegerField(blank=True)

class Habilidad(models.Model):
    name= models.CharField(max_length=30)
    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural='Skills'
        
    def __str__(self):
        return str(self.id) + '-' + self.name 

class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    short_name = models.CharField('Nombre corte', max_length=20, unique=True)
    anulate = models.BooleanField('anulado', default=False)
    
    class Meta:
        verbose_name = 'My Departament'
        verbose_name_plural= 'Departaments'
        ordering = ['-name']
        unique_together = ('name', 'short_name')
    

    def __str__(self):
        return str(self.id) + '-' + self.name + '-' + self.short_name  

