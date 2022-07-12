from FYP import settings
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.contrib.auth.base_user import BaseUserManager

class Trainer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)        
    trainer = models.BooleanField("trainer", default=True)
    gender = models.CharField(max_length=6, default="Male", blank=True) 
    trainer_image=models.ImageField(
        default='profile_pics/squat.webp',upload_to="profile_pics/"
    )
    qualification = models.TextField(null=True,blank=True)
    experience = models.TextField(null=True,blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.trainer_image.path)
        print("\n\n\n  -->  try saving image")
        width, height = img.size
        if height >= 300 or width >= 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            print("no error")
            img.save(self.trainer_image.path)
        else:
            print("no error saving")
            img.save(self.trainer_image.path)

    class Meta:
        db_table = "Trainer"
        verbose_name= "Trainers"
        verbose_name_plural="Trainers"

class Trainee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    trainee = models.BooleanField("trainee", default=True)
    trainer = models.ForeignKey(
        Trainer, blank=True, null=True, on_delete=models.SET_NULL
    )
    trainee_image=models.ImageField(
        default="profile_pics/squat.webp",upload_to="profile_pics/"
    )
    age = models.IntegerField(null=True,blank=True)
    gender = models.CharField(max_length=6, default="Male", blank=True) 
    trainee_level=models.CharField(max_length=100,null=True,blank=True)
    body_goal=models.CharField(max_length=100,blank=True)
    current_weight = models.DecimalField(max_digits=100, decimal_places=1,null=True,blank=True)
    goal_weight = models.DecimalField(max_digits=100, decimal_places=1,null=True,blank=True)
    body_fat = models.IntegerField(null=True,blank=True)
    height = models.DecimalField(max_digits=100, decimal_places=1,null=True,blank=True)
    trainee_level=models.CharField(max_length=100,null=True,blank=True)
    preferred_type_of_workout=models.CharField(max_length=100,null=True,blank=True)
    preferred_form_of_workout=models.CharField(max_length=100,null=True,blank=True)
    preferred_days_of_workout=models.CharField(max_length=100,null=True,blank=True)
    preferred_number_of_meals=models.CharField(max_length=100,null=True,blank=True)
    body_goal=models.CharField(max_length=100,null=True,blank=True)
    preferred_supplements=models.CharField(max_length=100,null=True,blank=True)


    def __str__(self):
        return f"{self.user.username} Profile"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.trainee_image.path)
        print("\n\n\n  -->  try saving image")
        width, height = img.size
        if height >=300 or width >= 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            print("no error")
            img.save(self.trainee_image.path)
        else:
            print("no error saving")
            img.save(self.trainee_image.path)

    class Meta:
        db_table = "Trainees"
        verbose_name= "Trainees"
        verbose_name_plural="Trainees"