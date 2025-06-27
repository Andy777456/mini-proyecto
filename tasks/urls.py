# tasks/urls.py
from django.urls import path
from . import views

# Define los patrones de URL para la aplicación 'tasks'.
urlpatterns = [
    path('', views.task_list, name='task_list'), # La ruta raíz de la aplicación mapea a la vista 'task_list'.
]
