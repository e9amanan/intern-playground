from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from django.contrib import messages
from django.http import JsonResponse
from .models import Task
from .forms import TaskForm, BaseTaskFormSet


def task_list(request):
    tasks = Task.objects.all()
    return render(request, "tasks/task_list.html", {"tasks": tasks})


# Formset for batch task creation
def batch_task_create(request):
    TaskFormSet = modelformset_factory(
        Task, form=TaskForm, formset=BaseTaskFormSet, extra=3
    )

    if request.method == "POST":
        formset = TaskFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            messages.success(request, "Batch tasks created successfully!")
            return redirect("task_list")
    else:
        formset = TaskFormSet(queryset=Task.objects.none())

    return render(request, "tasks/batch_create.html", {"formset": formset})


# AJAX Form Submission without page reload
def ajax_task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest"

        if form.is_valid():
            form.save()
            if is_ajax:
                return JsonResponse(
                    {"success": True, "message": "Task saved successfully!"}
                )
            return redirect("task_list")
        else:
            if is_ajax:
                return JsonResponse(
                    {"success": False, "errors": form.errors}, status=400
                )
    else:
        form = TaskForm()

    return render(request, "tasks/ajax_form.html", {"form": form})
