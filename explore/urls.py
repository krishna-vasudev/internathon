from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
   path('',views.explore,name='explore'),
   path('profile/<str:username>',views.profile,name='profile'),
   path('post',views.post,name='post'),
]
