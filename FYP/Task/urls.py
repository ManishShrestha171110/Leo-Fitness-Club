from django.urls import path
from . import views
from .views import DeleteTaskView
from django.contrib.auth import views as auth

urlpatterns = [
    path("donetask/<int:id>", views.done_task, name="donetask"),
    path("seetask", views.see_task, name="seetask"),
    path("seetaskfull/<int:id>", views.see_task_full, name="seetaskfull"),
    path("givetask/<str:username>", views.give_task, name="givetask"),
    path("deletetask/<int:pk>", DeleteTaskView.as_view(), name="deletetask"),
]
