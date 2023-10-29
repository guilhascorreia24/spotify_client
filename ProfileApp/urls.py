from django.contrib import admin
from django.urls import path
from . import views

name_app="ProfileAPP"
urlpatterns = [
    path('',views.Profile,name='profile'),
]