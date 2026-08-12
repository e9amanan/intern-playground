# todo/urls.py
from django.urls import path

from . import views

# Namespacing: this lets us refer to URLs as 'todo:task-list' later
app_name = "todo"

urlpatterns = [
    # 1. List View -> http://127.0.0.1:8000/todo/list/
    path("", views.task_list_fbv, name="task-list"),
    # 2. Detail View -> http://127.0.0.1:8000/todo/<slug>/
    path("<slug:slug>/", views.task_detail_fbv, name="task-detail"),
]
