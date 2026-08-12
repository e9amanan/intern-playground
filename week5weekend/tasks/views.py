from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Task
from .models import TaskForm
from django.db.models import Q

class TaskListView(ListView):
    model=Task
    template_name='tasks/task_list.html'
    context_object_name='tasks'
    paginate_by =10
    
    def get_queryset(self):
        queryset=super().get_queryset()

        search_query=self.request.GET.get('search')
        if search_query:
            queryset=queryset.filter(title__icontains=search_query)

        status=self.request.GET.get('status')
        priority=self.request.GET.get('priority')

        if status:
            queryset=queryset.filter(status=status)


