from .models import *
from django.forms import ModelForm,Textarea
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class TaskForm(ModelForm):
    class Meta:
        model =Task
        fields = ["task_title","task_goal","task_duration","task_content","task_note"]
        widgets = {
            'task_content': SummernoteWidget(),
            'task_note': SummernoteWidget(),
        }
