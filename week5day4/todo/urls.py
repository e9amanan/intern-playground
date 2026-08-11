from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.task_create, name='task_create'),
    path('<int:pk>/update/', views.task_update, name='task_update'),
]