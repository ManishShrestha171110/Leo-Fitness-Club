from django.shortcuts import render
from .models import *
from Users.models import Trainer
# Create your views here.
def home(request):
	trainer_home= Trainer.objects.all()
	context={
		'trainer_home':trainer_home
	}
	return render(request,'home.html',context)