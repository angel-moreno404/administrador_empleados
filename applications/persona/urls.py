from django.urls import path
from . import views

app_name="persona_app"

urlpatterns = [
    path('employs/', views.ListEmployer.as_view(), name='lista_employs'),
    path('employsarea/<short_name>/', views.ListByArea.as_view(), name='list-by-area'),
    path('employswork/<job>/', views.ListByWork.as_view()),
    path('buscar/', views.SearchByWord.as_view()),
    path('habilidades/', views.ListHabilidadesEmpleado.as_view()),
    path('datails/<pk>/', views.EmpleadoDetailView.as_view(), name="details"),
    path('create/', views.EmpleadoCreateView.as_view(), name='add_employed'),
    path('success/', views.SuccessViewp.as_view(), name='success'),
    path('update/<pk>/', views.UpdateEmpleado.as_view(), name='updated'),
    path('delete/<pk>/', views.EliminarEmpleado.as_view(), name='delete'),
    path('', views.HomeScreen.as_view(), name='home'),
    path('manage/', views.ListEmployeradmin.as_view(), name='manage'),    
    

    
      
     
    
]
