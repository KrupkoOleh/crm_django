from django import forms
from django.utils import timezone

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

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        project = cleaned_data.get('project')
        if Tasks.objects.filter(name=name, project=project).exists():
            raise forms.ValidationError("This task already exists")
        return cleaned_data


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

        def clean_deadline(self):
            deadline = self.cleaned_data.get('deadline')
            if deadline and deadline < timezone.now():
                raise forms.ValidationError("Дедлайн должен быть позже текущей даты и времени")
            return deadline

        def clean_name(self):
            name = self.cleaned_data.get('name')
            if name and Tasks.objects.filter(name=name, project=self.project).exclude(id=self.task_id).exists():
                raise forms.ValidationError("This name`s task already exists")
            return name
