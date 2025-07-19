from django.urls import path
from . import views

app_name = 'gastos_generales'

urlpatterns = [
    path('lista/', views.lista_gasto, name='lista_gasto'),
    path('eliminar_gasto/<int:id>/', views.eliminar_gasto, name='eliminar_gasto'),
    path('editar_gasto/', views.editar_gasto, name='editar_gasto'),
]
