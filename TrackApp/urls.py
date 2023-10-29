from django.contrib import admin
from django.urls import path
from . import views

name_app="TrackApp"
urlpatterns = [
    path('',views.Profile,name='track'),
]