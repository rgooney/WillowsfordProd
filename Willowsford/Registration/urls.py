from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('willowsfordWaiver', views.willowsfordWaiver, name='willowsfordWaiver'),
    path('archeryWaiver', views.archeryWaiver, name='archeryWaiver'),
    path('rulesOfConductWaiver', views.rulesOfConductWaiver, name='rulesOfConductWaiver'),
    path('guestRegistration', views.guestRegister, name='guestRegistration'),
]