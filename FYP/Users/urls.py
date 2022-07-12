from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth
from .views import DeleteUserView

urlpatterns = [
    path("traineeregister/", views.trainee_register, name="traineeregister"), 
    path("login/", views.auth_login, name="login"),
    path("logout/", auth.LogoutView.as_view(template_name="login.html"), name="logout"),
    path("selecttrainer/", views.select_trainer, name="selecttrainer"),
    path("givetraineedetail/", views.give_trainee_detail, name="givetraineedetail"),
    path("seetraineedetail/<int:id>", views.see_trainee_detail, name="seetraineedetail"),
    path(
        "traineeprofileupdate/", views.trainee_profile_update, name="traineeprofileupdate"
    ),
    path(
        "trainerprofileupdate/", views.trainer_profile_update, name="trainerprofileupdate"
    ),
    path("traineeprofile/", views.trainee_profile, name="traineeprofile"),
    path("trainerprofile/", views.trainer_profile, name="trainerprofile"),
    path("deleteuser/<int:pk>", DeleteUserView.as_view(), name="deleteuser"),
    path("password_reset/", auth.PasswordResetView.as_view(template_name='password_reset_form.html'),  name="password_reset"),
    path("password_reset/done/", auth.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name="password_reset_confirm"),
    path("reset/done/", auth.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name="password_reset_complete"),
]