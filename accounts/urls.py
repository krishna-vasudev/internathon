from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("login", views.loginUser, name='login'),
    path("logout", views.logoutuser, name='logout'),
    path("signup", views.signupuser, name='signup'),
]


