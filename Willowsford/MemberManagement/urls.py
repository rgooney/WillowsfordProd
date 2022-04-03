from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signIn', views.signIn, name='signIn'),
    path('dashboard', views.dashboard, name='dashboard'),
]