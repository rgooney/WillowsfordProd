from django.urls import path
from . import views
from django.urls import re_path
#from django.conf.urls import url

urlpatterns = [
    path('manualScoring', views.manualScoring, name="manualScoring"),
]