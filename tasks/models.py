from django.db import models
from django.utils import timezone

class Task(models.Model):
    """
    Representa una tarea en la lista de tareas.
    """
    # Título de la tarea, es un campo de texto corto y obligatorio.
    title = models.CharField(max_length=200)
    # Descripción detallada de la tarea, es opcional.
    description = models.TextField(blank=True, null=True)
    # Fecha y hora en que se creó la tarea. Se establece automáticamente al crear.
    created_at = models.DateTimeField(auto_now_add=True)
    # Fecha y hora en que se completó la tarea. Es opcional.
    completed_at = models.DateTimeField(blank=True, null=True)
    # Fecha y hora de vencimiento de la tarea. Es opcional.
    due_date = models.DateTimeField(blank=True, null=True)
    # Nombre del autor de la tarea. Es opcional.
    author = models.CharField(max_length=100, blank=True, null=True)
    # Campo booleano para indicar si la tarea está completada o no. Por defecto es False.
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        # Devuelve el título de la tarea como su representación en cadena.
        return self.title
