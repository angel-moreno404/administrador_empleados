from django.contrib import admin
from .models import Persona, Habilidad

# Register your models here.

admin.site.register(Habilidad)
class Empleadoadmin(admin.ModelAdmin):
    list_display=( 
    'first_name',
    'last_name',
    'job', 
    'departamento',
    'full_name',
    'id',
    )
    def full_name(self, obj):
        
        return obj.first_name+' '+obj.last_name
    search_fields=('first_name',)
    list_filter = ('departamento','job','habilidad',)
    filter_horizontal = ('habilidad',)
admin.site.register(Persona, Empleadoadmin )
