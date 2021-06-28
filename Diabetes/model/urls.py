from os import name
from django.contrib import admin
from django.urls import path,include
from model import views as v

urlpatterns = [
    path('front',v.front,name="front"),
    path('predict/',v.predict,name="predictd"),
    path('predict/result',v.result),
    path('register',v.reg),
    path('login',v.mylogin,name="login"),
    path('logout',v.logoutUser,name="logout"),
    path('about',v.about,name="about"),
    
]

