from django import forms
from .models import Tasks


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Start typing here to create the task...'
            })
        }


class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['name', 'deadline', 'status']
        widgets = {
            'deadline': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control'
            })
        }
