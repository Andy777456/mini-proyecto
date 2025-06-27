from django.shortcuts import render, redirect
from .models import Task
from django.utils import timezone

def task_list(request):
    if request.method == 'POST':
        # Maneja la eliminación de una tarea.
        if 'delete' in request.POST:
            task_id = request.POST.get('delete')
            Task.objects.filter(id=task_id).delete()
        # Maneja el cambio de estado (completado/no completado) de una tarea.
        elif 'complete' in request.POST:
            task_id = request.POST.get('complete')
            task = Task.objects.get(id=task_id)
            # Invierte el estado de completado.
            task.is_completed = not task.is_completed
            # Establece o borra la fecha de completado según el estado.
            task.completed_at = timezone.now() if task.is_completed else None
            task.save()
        # Maneja la actualización de una tarea existente.
        elif 'update' in request.POST:
            task_id = request.POST.get('update')
            task = Task.objects.get(id=task_id)
            # Actualiza el título de la tarea.
            task.title = request.POST.get(f'title_{task_id}')
            # Actualiza la descripción, usando una cadena vacía si no se proporciona.
            task.description = request.POST.get(f'description_{task_id}', '')
            # Actualiza la fecha de vencimiento, o None si está vacía.
            task.due_date = request.POST.get(f'due_date_{task_id}') or None
            # Actualiza el autor, usando una cadena vacía si no se proporciona.
            task.author = request.POST.get(f'author_{task_id}', '')
            task.save()
        # Maneja la creación de una nueva tarea.
        else:
            # Obtiene los datos del formulario para la nueva tarea.
            title = request.POST.get('title')
            description = request.POST.get('description', '')
            due_date = request.POST.get('due_date') or None
            author = request.POST.get('author', '')
            # Crea una nueva instancia de Task en la base de datos.
            Task.objects.create(
                title=title,
                description=description,
                due_date=due_date,
                author=author
            )
        # Redirige a la misma página para evitar el reenvío del formulario.
        return redirect('task_list')
    
    # Si la solicitud es GET, o después de procesar un POST, recupera todas las tareas.
    # Las ordena por fecha de creación en orden descendente (las más recientes primero).
    tasks = Task.objects.all().order_by('-created_at')
    # Renderiza la plantilla 'task_list.html' pasando la lista de tareas.
    return render(request, 'tasks/task_list.html', {'tasks': tasks})