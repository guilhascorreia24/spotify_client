from django.contrib import admin
from django.urls import path
from . import views

name_app="TrackApp"
urlpatterns = [
    path('',views.Tracks,name='library'),
    path('playlist/<str:id>',views.Playlist,name='playlist')
]