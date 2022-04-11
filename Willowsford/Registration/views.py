from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .forms import *

# Create your views here.
def register(request):
    if request.POST:
        user_form = UserAccountForm(request.POST)
        extended_user_form = RegistrationForm(request.POST)
        if user_form.is_valid() and extended_user_form.is_valid():
            user = user_form.save(commit=False)
            user.save()
            extended_user_info = extended_user_form.save(commit=False)
            extended_user_info.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        user_form = UserAccountForm()
        extended_user_form = RegistrationForm()

    return render(request, 'Registration/registration.html', {'user_form': user_form, 'extended_user_form': extended_user_form})

# def registerptwo(request, user_fk):
#     user_account = User.objects.get(username=user_fk)
#     if request.POST:
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.username = user_account
#             user.save()
#             return HttpResponseRedirect(reverse('index'))
#         # else:
#         #     return render(request, 'registration/registration.html', {'form': form})
#     else:
#         form = RegistrationForm()
#
#     return render(request, 'Registration/registration2.html', {'form': form, 'username': user_fk})

