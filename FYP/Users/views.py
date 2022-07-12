from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from .forms import *
from Task.models import Task
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DeleteView
from django.contrib.auth.models import User
from django.template.loader import get_template
from django.template import Context
from FYP import settings
from django.urls import reverse_lazy

def trainee_register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        Tform = TraineeRegisterForm(request.POST, request.FILES)
        if form.is_valid() and Tform.is_valid():

            user = form.save()
            profile = Tform.save(commit=False)
            profile.user = user
            profile.save()

            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            messages.info(
                request, "Your account has been created! You are now able to log in"
            )
            return redirect("login")
    else:
        form = UserRegisterForm()
        Tform = TraineeRegisterForm()

    return render(request, "trainee_register.html", {"form": form, "tform": Tform})
    

def auth_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)
        if user is not None:
            try:
                trainer = Trainer.objects.get(user=user)
            except:
                trainer = False
            if trainer:
                
                login(request, user)
                messages.success(request, f" welcome {username} !!")
                try:
                    trainee = Trainee.objects.filter(trainer=trainer)
                except:
                    trainee = None
                print("---------------------------------")
                data = {"trainee": trainee}
                return render(request, "trainerdashboard.html", data)

            else:
                login(request,user)
                try:
                    task = Task.objects.filter(
                        person=Trainee.objects.get(user=request.user)
                    )
                except:
                    task = None
                data = {"task": task}
                messages.success(request, f" wecome {username} !!")
                return render(request, "traineedashboard.html")

        else:
            messages.info(request, f"Account does not exist. Please register")
            
    if request.user.is_anonymous:
        form = LoginForm()
        return render(request, "login.html", {"form": form})
    else:
        try:
            trainer = Trainer.objects.get(user=request.user)
        except:
            trainer = False
        if trainer:
            try:
                trainee = Trainee.objects.filter(trainer=trainer)
            except:
                trainee = None

            data = {"trainee": trainee}
            return render(request, "trainerdashboard.html", data)
            
        else:
            try:
                task = Task.objects.filter( 
                    person=Trainee.objects.get(user=request.user)
                )
            except:
                task = None
            data = {"task": task}
            return render(request, "traineedashboard.html", data)

@login_required
def see_trainee_detail(request,id):
    trainee = Trainee.objects.get(id=id)
    data = {"trainee": trainee}
    return render(request, "see_trainee_detail.html", data)


@login_required
def trainee_profile_update(request):
    if request.method == "POST":
        uform=UserUpdateForm(request.POST,request.FILES,instance=request.user)
        form = TraineeUpdateForm(request.POST,request.FILES,instance=request.user.trainee)
        print('\n\n\n\n\n-->',form.errors)
        if uform .is_valid and form.is_valid():
            uform.save()
            form.save()
            messages.success(request, f"profile is updated")
            return redirect("traineeprofile")

    uform = UserUpdateForm(instance=request.user)
    form = TraineeUpdateForm(instance=request.user.trainee)
    data = {
        'uform':uform,
        "form": form,
        "profile_pic": request.user.trainee.trainee_image.url,
        "title": "profile update for {}".format(request.user),
    }
    return render(request, "traineeprofileupdate.html", data)

@login_required
def select_trainer(request):
    if request.method == "POST":
        form = SelectTrainerForm(request.POST,request.FILES,instance=request.user.trainee)
        print('\n\n\n\n\n-->',form.errors)
        if form.is_valid():
            form.save()
            messages.success(request, f"Trainer is selected")
            return redirect("login")
    
    form = SelectTrainerForm(instance=request.user.trainee)
    trainer=Trainer.objects.all()
    data = {
        'trainer' : trainer,
        "form": form,
        "title": "Trainer selected for {}".format(request.user),
    }
    return render(request, "select_trainer.html", data)

@login_required
def give_trainee_detail(request):
    if request.method == "POST":
        form = TraineeDetailForm(request.POST,request.FILES,instance=request.user.trainee)
        print('\n\n\n\n\n-->',form.errors)
        if form.is_valid():
            form.save()
            messages.success(request, f"Detail provided to Trainer")
            return redirect("login")

    form = TraineeDetailForm(instance=request.user.trainee)
    data = {
        "form": form,
        "title": "Trainer selected for {}".format(request.user),
    }
    return render(request, "give_trainee_detail.html", data)


@login_required
def trainer_profile_update(request):
    if request.method == "POST":
        uform=UserUpdateForm(request.POST,request.FILES,instance=request.user)
        form = TrainerUpdateForm(request.POST,request.FILES,instance=request.user.trainer)
        print('\n\n\n\n\n-->',form.errors)
        if form.is_valid():
            form.save()
            messages.success(request, f"profile is updated")
            return redirect("trainerprofile")

    uform = UserUpdateForm(instance=request.user)
    form = TrainerUpdateForm(instance=request.user.trainer)
    data = {   
        'uform':uform, 
        "form": form,
        "title": "profile update for {}".format(request.user),
    }   
    return render(request, "trainerprofileupdate.html", data)

@login_required
def trainee_profile(request):
    data = {"profile_pic": request.user.trainee.trainee_image.url}
    return render(request, "profile.html",data)

@login_required
def trainer_profile(request):
    data = {"profile_pic": request.user.trainer.trainer_image.url}
    return render(request, "profile.html",data)

class DeleteUserView(DeleteView):
    model=User
    template_name='delete.html'
    success_url=reverse_lazy('home')