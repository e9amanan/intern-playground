from django import forms
from .models import Task
from django.utils import timezone

class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['title','description','status','priority','due_date','category','tags']
        widgets={
            'due_date': forms.DateInput(attrs={'type':'date'}),
        }

    def clean_title(self):
        title=self.cleaned_data.get('title')
        if title and len(title.strip())<3:
            raise forms.ValidationError("title must be atleast 3 characters long")
        return title

    def clean_due_date(self):
        due_date=self.cleaned_data.get('due_date')
        if due_date and due_date < timezone.now().date():
            raise forms.ValidationError("due date cannot be in the past.")
        return due_date