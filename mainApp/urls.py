from django.contrib import admin
from django.urls import path
from . import views

name_app="mainApp"
urlpatterns = [
    path('home',views.home,name='home'),
    path('',views.login_logout)
]