from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path(r'^signout/$', views.SignOut.as_view(), name='signout'),
    path('response/', views.responseView, name='response'),
]