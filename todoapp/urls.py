from django.urls import path
from todoapp.views import RegisterUserView,HomeView,LoginUserView,AddTaskView,DeleteTask


app_name="todo"
urlpatterns = [
    path("",RegisterUserView.as_view(),name="register"),
    path("home/",HomeView.as_view(),name="home"),
    path("login/",LoginUserView.as_view(),name="login"),
    path("add-post/",AddTaskView.as_view(),name="taskadd"),
    path("delete-task/<int:id>/",DeleteTask.as_view(),name="delete-task")
]
