from django.urls import path
from . import views
from django.urls import re_path
#from django.conf.urls import url

urlpatterns = [
    path('manualScoring', views.manualScoring, name="manualScoring"),
    path('calculateScore', views.calculateScore, name="calculateScore"),
    path('receiveInput', views.receiveInput, name="receiveInput"),
]