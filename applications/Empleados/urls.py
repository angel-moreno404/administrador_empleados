from django.urls import path
from . import views

urlpatterns = [
    path('empleados/', views.IndexView.as_view()),
    path('fundation/', views.PruebaFundation.as_view()),
    path('prueba1/', views.Prueba1.as_view()),
    path('prueba2/', views.Prueba2.as_view()),
    path('prueba3/', views.Prueba3.as_view()),
    
]
