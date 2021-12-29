from django.urls import path
from . import views

urlpatterns = [
    path("",views.top, name="top"),
    path("about",views.about,name="about"),
    path("signup",views.signup,name="signup"),
    path("login",views.login,name="login"),
    path("index",views.index, name="index"),
    path("add",views.add ,name="add"),
    path("edit/<int:num>", views.edit, name="edit"),
    path("delete/<int:num>",views.delete,name="delete"),
]
