from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('batch-create/', views.batch_task_create, name='batch_task_create'),
    path('ajax-create/', views.ajax_task_create, name='ajax_task_create'),
]