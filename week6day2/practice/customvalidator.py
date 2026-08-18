from django.core.exceptions import ValidationError
from django import forms
from tasks.models import Task


def validate_no_profanity(value:str)-> None:
    #function based custom validator
    bad_words=['spam','fake','test']

    for word in bad_words:
        
        if word in value.lower():
            raise ValidationError(
                f"The word '{word}' is not allowed.",
                code='invalid_word'
            )

class TaskForm(forms.ModelForm):
        title= forms.CharField(validators=[validate_no_profanity])

        class Meta:
            model = Task
            fields=['title','description','due_date','status']

        def clean_title(self):
            title=self.cleaned_data.get('title')

            if len(title)<5:
                raise forms.ValidationError("Title must be at least 5 characters long.")

            return title