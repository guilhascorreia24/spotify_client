from django.contrib import admin
from django.urls import path
from . import views

name_app="history"
urlpatterns = [
    path('',views.getHistory,name='history'),
    path('after/<str:after>/before/<str:before>/',views.getHistory,name='history_with_timestamp'),
]