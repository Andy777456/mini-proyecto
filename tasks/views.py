from django.shortcuts import render, redirect
from .models import Task
from django.utils import timezone

def task_list(request):
    if request.method == 'POST':
        if 'delete' in request.POST:
            task_id = request.POST.get('delete')
            Task.objects.filter(id=task_id).delete()
        elif 'complete' in request.POST:
            task_id = request.POST.get('complete')
            task = Task.objects.get(id=task_id)
            task.is_completed = not task.is_completed
            task.completed_at = timezone.now() if task.is_completed else None
            task.save()
        elif 'update' in request.POST:
            task_id = request.POST.get('update')
            task = Task.objects.get(id=task_id)
            task.title = request.POST.get(f'title_{task_id}')
            task.description = request.POST.get(f'description_{task_id}', '')
            task.due_date = request.POST.get(f'due_date_{task_id}') or None
            task.author = request.POST.get(f'author_{task_id}', '')
            task.save()
        else:
            title = request.POST.get('title')
            description = request.POST.get('description', '')
            due_date = request.POST.get('due_date') or None
            author = request.POST.get('author', '')
            Task.objects.create(
                title=title,
                description=description,
                due_date=due_date,
                author=author
            )
        return redirect('task_list')
    
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})