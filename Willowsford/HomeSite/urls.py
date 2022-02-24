from django.contrib import admin
from django.urls import path
from . import views

urlspatterns = [
    path('', views.index, name="index"),
]