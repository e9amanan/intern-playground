from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task


class SignupView(CreateView):
    #signup page
    
    form_class = UserCreationForm 
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('task-list')

    
    def form_valid(self, form):
       #direct login after signup
        user = form.save()
        
        login(self.request, user)
        
        return super().form_valid(form)


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks' 

    
    def get_queryset(self):
        # filter the database and return task of selected owner only.
        
        return Task.objects.filter(owner=self.request.user)


class TaskCreateView(LoginRequiredMixin, CreateView):
    #creating task
    model = Task
    
    fields = ['title'] 
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task-list')

    
    def form_valid(self, form):
        #attach their User ID to it
        form.instance.owner = self.request.user
        return super().form_valid(form)
