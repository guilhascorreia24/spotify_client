from django.contrib import admin
from django.urls import path
from . import views

name_app="PlayerApp"
urlpatterns = [
    path('player/<str:id>',views.player,name='player'),
]