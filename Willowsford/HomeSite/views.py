from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'HomeSite/index.html')

def about(request):
    return render(request, 'HomeSite/about.html')

def services(request):
    return render(request, 'HomeSite/services.html')