from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_title', 'task_description', 'task_file', 'task_url', 'task_status']

    def clean_task_title(self):
        task_title = self.cleaned_data.get('task_title')
        if len(task_title) < 5:
            raise forms.ValidationError('Task title must be at least 5 characters long.')
        return task_title
