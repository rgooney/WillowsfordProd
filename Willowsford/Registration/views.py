from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .forms import *

# Create your views here.
def registerpone(request):
    if request.POST:
        form = UserAccountForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return HttpResponseRedirect(reverse('registerptwo', args=[user.username]))
    else:
        form = UserAccountForm()

    return render(request, 'Registration/registration.html', {'form': form})

def registerptwo(request, user_fk):
    user_account = User.objects.get(username=user_fk)
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user_account
            user.save()
            return HttpResponseRedirect(reverse('index'))
        # else:
        #     return render(request, 'registration/registration.html', {'form': form})
    else:
        form = RegistrationForm()

    return render(request, 'Registration/registration2.html', {'form': form, 'username': user_fk})

