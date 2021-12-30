from django.urls import path
from . import views
from .views import AppsDetail
urlpatterns = [
    path("",views.top, name="top"),
    path("about",views.about,name="about"),
    path("signup",views.signup,name="signup"),
    path("login",views.login,name="login"),
    path("index",views.index, name="index"),
    path("<int:num>",views.index, name="index"),
    path("add",views.add ,name="add"),
    path("edit/<int:num>", views.edit, name="edit"),
    path("delete/<int:num>",views.delete,name="delete"),
    path("find",views.find, name="find"),
    path("detail/<int:pk>",AppsDetail.as_view(),name="detail")
]
