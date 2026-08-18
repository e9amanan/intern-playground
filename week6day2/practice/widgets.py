from django import forms
from tasks.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['title','description','due_date','status']

        widgets={
            'description':forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Enter detailed task instructions here '
            }),
            
            'due_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type':'date'
            }),
            
            'status': forms.Select(attrs={
                'class': 'form-select'
            })
        }