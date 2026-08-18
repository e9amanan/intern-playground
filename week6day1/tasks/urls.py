from django.urls import path
from .views import TaskListView, TaskCreateView, SignupView

urlpatterns = [
    # The homepage (empty string '') triggers the TaskListView
    path('', TaskListView.as_view(), name='task-list'),
    
    # Going to /new/ triggers the TaskCreateView
    path('new/', TaskCreateView.as_view(), name='task-create'),
    
    # Going to /accounts/signup/ triggers our custom SignupView
    path('accounts/signup/', SignupView.as_view(), name='signup'),
]