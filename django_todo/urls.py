"""
URL configuration for django_todo project.

La lista `urlpatterns` enruta las URLs a las vistas. Para más información, consulta:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Añade una importación:  from my_app import views
    2. Añade una URL a urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Añade una importación:  from other_app import Home
    2. Añade una URL a urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Importa la función include(): from django.urls import include, path
    2. Añade una URL a urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# Define las rutas URL para el proyecto.
urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para la interfaz de administración de Django.
    path('', include('tasks.urls')),  # Incluye las URLs de la aplicación 'tasks' en la raíz del proyecto.
]
