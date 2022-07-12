from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from Users.models import *
from .forms import *
from .models import *
from django.views.generic import DeleteView
from django.urls import reverse_lazy

@login_required
def give_task(request, username):
    if request.method == "POST":
        task_form = TaskForm(request.POST)
        print(task_form.errors)
        if task_form.is_valid():
            trainee_here = Trainee.objects.get(user__username=username)
            task_title=request.POST["task_title"]
            task_goal = request.POST["task_goal"]
            task_duration = request.POST["task_duration"]
            task_content = request.POST["task_content"]
            task_note = request.POST["task_note"]

            Task.objects.create(
                person=trainee_here,task_title=task_title,task_goal=task_goal,task_duration=task_duration,task_content=task_content,task_note=task_note
            )
            messages.success(request, f"task given to user")

    task_form = TaskForm() 
    data = {"task_form": task_form, "username": username}
    return render(request, "givetask.html", data)

@login_required
def see_task(request):
    data = {"task": Task.objects.filter(person=Trainee.objects.get(user=request.user))}
    return render(request, "seetask.html", data)

@login_required
def see_task_full(request,id):
    task = Task.objects.get(id=id)
    data = {"task": task}
    return render(request, "task_full.html", data)

@login_required
def done_task(request,id):
    task = Task.objects.get(id=id)
    task.task_complete = True
    task.save()
    print(Task.objects.get(id=id).task_complete)
    return redirect("seetask")

class DeleteTaskView(DeleteView):
    model=Task
    template_name='delete_task.html'
    success_url=reverse_lazy('seetask')
