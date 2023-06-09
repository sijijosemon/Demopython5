
from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [

    path('',views.index,name="index"),
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('loggedin', views.loggedin, name="loggedin"),
    path('regform',views.regform,name="regform"),
    path('confirm',views.confirm,name='confirm'),
    path('logout',views.logout,name='logout'),
]