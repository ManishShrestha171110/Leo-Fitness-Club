from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordChangeForm
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Field
from django import forms
from django.forms import Textarea
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

Gender=[
    ('Male','Male'),
    ('Female','Female'),
]
Trainee_Level=[
    ('Beginner','Beginner'),
    ('Intermediate','Intermediate'),
    ('Advanced','Advanced'),
]
Body_Goal=[
    ('Muscle Building','Muscle Building'),
    ('Fat Loss','Fat Loss'),
    ('Stay Fit','Stay Fit'),
    ('Increase strength','Increase Strength'),
]
Preferred_Form_Of_Workout=[
    ('Weighlifting at gym','Weightlifting at gym'),
    ('Home Workout','Home Workout'),
    ('Calisthenics ','Calistheics'),
    ('Other','Other'),
]
Preferred_Type_Of_Workout=[
    ('Full Body Workout','Full Body Workout'),
    ('Push/Pull/Legs','Push/Pull/Legs'),
    ('One muscle per day ','One muscle per day'),
    ('Two muscles per day','Two muscles per day'),
    ('Other','Other'),
]
Preferred_Days_Of_Workout=[
    ('Three Days','Three Days'),
    ('Four Days','Four Days'),
    ('Five Days','Five Days'),
    ('Six Days','Six Days'),
    ('Seven Days','Seven Days'),
]
Preferred_Number_Of_Meals=[
    ('Three Meals','Three Meals'),
    ('Four Meals','Four Meals'),
    ('Five Meals','Five Meals'),
    ('Six Meals','Six Meals'),
    ('Seven Meals','Seven Meals'),

]
Preferred_Supplements=[
    ('Yes','Yes'),
    ('No','No'),
]
class UserRegisterForm(UserCreationForm):
    password2=forms.CharField(
        widget=forms.PasswordInput(),
        label="Confirm Password: ",
    )
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        ]
        
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
        return email

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm,self).__init__(*args, **kwargs)
        
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class LoginForm(AuthenticationForm):
    username=forms.CharField(
        widget=forms.TextInput(attrs={'class':'input-container'}),
        label="",
    )
    password=forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'input-container', 'id':'password'}),
        label="",
    )

    class Meta:
        model = User
        fields = [
            "username",
            "password",
        ]


class TraineeRegisterForm(ModelForm):
    gender=forms.ChoiceField(choices=Gender)
    class Meta:
        model = Trainee
        exclude = ("trainee","user",'trainer','age','trainee_level','body_goal','current_weight','goal_weight','body_fat','height','preferred_type_of_workout','preferred_form_of_workout','preferred_days_of_workout','preferred_number_of_meals','body_goal','preferred_supplements')

class SelectTrainerForm(ModelForm):
    class Meta:
        model=Trainee
        fields=['trainer']

class TraineeDetailForm(ModelForm):
    gender=forms.ChoiceField(choices=Gender)
    trainee_level=forms.ChoiceField(choices=Trainee_Level)
    preferred_type_of_workout=forms.ChoiceField(choices=Preferred_Type_Of_Workout)
    preferred_form_of_workout=forms.ChoiceField(choices=Preferred_Form_Of_Workout)
    preferred_days_of_workout=forms.ChoiceField(choices=Preferred_Days_Of_Workout)
    preferred_number_of_meals=forms.ChoiceField(choices=Preferred_Number_Of_Meals)
    body_goal=forms.ChoiceField(choices=Body_Goal)
    preferred_supplements=forms.ChoiceField(choices=Preferred_Supplements)
    class Meta:
        model=Trainee
        fields=['gender','age','trainee_level','body_goal','height','current_weight','goal_weight','body_fat','preferred_type_of_workout','preferred_form_of_workout','preferred_days_of_workout','preferred_number_of_meals','preferred_supplements']

class UserUpdateForm(ModelForm):
    class Meta:
        model=User
        fields=['username','email',]


class TraineeUpdateForm(ModelForm):
    gender=forms.ChoiceField(choices=Gender)
    class Meta:
        model = Trainee
        exclude = ("trainee", "user",'trainer','age','trainee_level','body_goal','current_weight','goal_weight','body_fat','height','preferred_type_of_workout','preferred_form_of_workout','preferred_days_of_workout','preferred_number_of_meals','body_goal','preferred_supplements')

class TrainerUpdateForm(ModelForm):
    class Meta:
        model = Trainer
        exclude=("user","trainer")
        widgets = {
            'qualification': SummernoteWidget(),
            'experience': SummernoteWidget(),
        }