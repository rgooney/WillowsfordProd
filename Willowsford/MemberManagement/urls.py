from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signIn', views.signIn, name='signIn'),
    path('adminPanel', views.adminPanel, name='adminPanel'),
]