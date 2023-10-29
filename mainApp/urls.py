from django.contrib import admin
from django.urls import path
from . import views

name_app="mainApp"
urlpatterns = [
    path('',views.home,name='home'),
]