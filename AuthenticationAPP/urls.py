from django.contrib import admin
from django.urls import path
from . import views

name_app="authentication"
urlpatterns = [
    path('login/',views.spotify_login,name='login'),
    path('logout/',views.spotify_logout,name='logout'),
    path('callback/',views.callback,name='callback')
]