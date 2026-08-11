from django import forms
from django.core.exceptions import ValidationError
from datetime import date
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['project', 'title', 'description', 'start_date', 'due_date', 'is_completed']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }

    # Validation 1: Prevent past dates
    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if due_date and due_date < date.today():
            raise ValidationError("The due date cannot be in the past!")
        return due_date

    # Validation 2: Ensure due date is after start date
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        due_date = cleaned_data.get('due_date')

        if start_date and due_date and due_date < start_date:
            raise ValidationError("Due date must come after the start date.")
        return cleaned_data