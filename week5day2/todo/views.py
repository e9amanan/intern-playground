from django.db import models
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Task


def task_list_fbv(request):
    """
    FBV to display a list of all tasks.
    """
    # 1. Fetch all tasks from the database, newest first
    tasks = Task.objects.all().order_by("-created_at")

    # 2. Package the data into a dictionary called 'context'
    context = {
        "tasks": tasks,
    }

    # 3. Combine the request, HTML template, and context data into an HttpResponse
    return render(request, "todo/task_list.html", context)


def task_detail_fbv(request, slug):
    """
    FBV to display a single task based on its slug.
    """
    # 1. Safely query for the task matching this slug, or return 404 Not Found
    task = get_object_or_404(Task, slug=slug)

    # 2. Package into context
    context = {
        "task": task,
    }

    # 3. Render and return response
    return render(request, "todo/task_detail.html", context)


def ping_fbv(request):
    """
    Demonstrates returning a raw HttpResponse directly from Python.
    """
    return HttpResponse("<h1>Server Status: OK</h1><p>No template file needed!</p>")


def complete_task_fbv(request, slug):
    """
    Demonstrates modifying data and using redirect() to send the user elsewhere.
    """
    # 1. Find the task
    task = get_object_or_404(Task, slug=slug)

    # 2. Mark it as complete and save to the database
    task.completed = True
    task.save()

    # 3. Redirect the browser back to the task detail page
    return redirect("todo:task-detail", slug=task.slug)


# 1. LIST VIEW (with Pagination & Method Overrides)
class TaskListView(ListView):
    model = Task
    template_name = "todo/task_list.html"
    context_object_name = "tasks"
    paginate_by = 5  # Shows 5 tasks per page!

    def get_queryset(self):
        """
        Override default query to sort by newest tasks first.
        """
        return Task.objects.all().order_by("-created_at")

    def get_context_data(self, **kwargs):
        """
        Override context to inject extra custom variables into HTML.
        """
        context = super().get_context_data(**kwargs)
        context["page_title"] = "All Tasks Overview"
        return context


# 2. DETAIL VIEW
class TaskDetailView(DetailView):
    model = Task
    template_name = "todo/task_detail.html"
    context_object_name = "task"


# 3. CREATE VIEW
class TaskCreateView(CreateView):
    model = Task
    template_name = "todo/task_form.html"
    fields = ["title", "slug", "description", "completed"]


# 4. UPDATE VIEW
class TaskUpdateView(UpdateView):
    model = Task
    template_name = "todo/task_form.html"
    fields = ["title", "slug", "description", "completed"]


# 5. DELETE VIEW
class TaskDeleteView(DeleteView):
    model = Task
    template_name = "todo/task_confirm_delete.html"
    success_url = reverse_lazy("todo:task-list")
