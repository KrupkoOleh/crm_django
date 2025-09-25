from django import forms
from .models import Tasks


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Start typing here to create the task...'
            })
        }
