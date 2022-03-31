from django.shortcuts import render

# Create your views here.
def registerpone(request):
    return render(request, 'Registration/registration.html')

def registerptwo(request):
    return render(request, 'Registration/registration2.html')

