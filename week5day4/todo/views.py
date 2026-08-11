from django.shortcuts import render
from django.shortcuts import redirect
from .models import Task
from django.contrib import messages
from .forms import TaskForm
from django.shortcuts import get_object_or_404 

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task successfully created!')
            return redirect('task_create') # Reloads the page after saving
        else:
            messages.error(request, 'Error saving task. Please fix the issues below.')
    else:
        form = TaskForm()
    
    return render(request, 'todo/task_form.html', {'form': form})

def task_update(request, pk):
    # Fetch the specific task by its ID 
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        # instance=task tells Django to update this exact row, not make a new one
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task successfully updated!')
            return redirect('task_update', pk=task.pk)
        else:
            messages.error(request, 'Error updating task. Please fix the issues below.')
    else:
        
        form = TaskForm(instance=task)
    
    return render(request, 'todo/task_form.html', {'form': form})