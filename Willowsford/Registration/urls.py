from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('registerpone', views.registerpone, name='registerpone'),
    path('registerptwo/<str:user_fk>', views.registerptwo, name='registerptwo'),
]