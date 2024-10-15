
from django.urls import path
from . import views

app_name='departamento_app'
urlpatterns = [
    path('home/', views.IndexView.as_view()),
    path('lista_prueba', views.PruebaListView.as_view()),
    path('lista_prueba_m', views.ModeloTryListView.as_view()),
    path('form_prueba', views.FormPrueba.as_view()),
    path('new_departament', views.NewRegisterDepartament.as_view(),name='create_new_departament'),
    path('list-departament', views.DepartamentoListView.as_view(),name='list-departament'),
    
]
