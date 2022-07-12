from django.db import models
from Users.models import *


class Task(models.Model):
    person = models.ForeignKey(
        Trainee, on_delete=models.CASCADE, unique=False, default=""
    )
    task_complete = models.BooleanField(default=False)
    task_title=models.CharField(max_length=100)
    task_goal=models.CharField(max_length=100)
    task_duration=models.CharField(max_length=100)
    task_content=models.TextField()
    task_note=models.TextField()

    def __str__(self):
        return f"{self.person}"
    
    class Meta:
        db_table="task"