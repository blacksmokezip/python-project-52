from django import forms
from django.utils.translation import gettext_lazy as _

from task_manager.tasks.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'status', 'executor', 'labels')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': _("Name")}),
            'description': forms.Textarea(attrs={'placeholder': _("Description")}),
        }
        labels = {
            'name': _("Name"),
            'description': _("Description"),
            'status': _("Status"),
            'executor': _("Executor"),
            'labels': _("Labels"),
        }
