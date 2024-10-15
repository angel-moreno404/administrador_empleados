from django import forms

from .models import Prueba
class NewDepartament(forms.Form):
    nombre= forms.CharField(max_length=50)
    apellidos= forms.CharField(max_length=50)
    departamento= forms.CharField(max_length=50)
    nombre_corto= forms.CharField(max_length=20)
    
class PruebaForm(forms.ModelForm):
    class Meta:
        model=Prueba
        fields=['title', 'subtitle', 'cantidad']
        widgets={
            'title':forms.TextInput(
                attrs={
                    'placeholder':'ingrese el titulo aqui'
                }
            )
        }
    def clean_cantidad(self):
        cantidad= self.cleaned_data['cantidad']
        if cantidad < 10:
            raise forms.ValidationError('la cantidad es menor a 10')
        return cantidad
