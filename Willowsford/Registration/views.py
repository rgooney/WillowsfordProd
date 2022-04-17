from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .forms import *
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.
def register(request):
    if request.POST:
        user_form = UserAccountForm(request.POST)
        extended_user_form = RegistrationForm(request.POST)
        if user_form.is_valid() and extended_user_form.is_valid():
            user = user_form.save()
            extended_user_info = extended_user_form.save(commit=False)
            extended_user_info.user = user


            extended_user_info.save()

            return HttpResponseRedirect(reverse('index'))
        else:
            print(user_form.errors)
            print(extended_user_form.errors)
            return render(request, 'Registration/registration.html',
                          {'user_form': user_form, 'extended_user_form': extended_user_form})
            # return render(request, 'Registration/registration.html', {'extended_user_form': extended_user_form})
    else:
        user_form = UserAccountForm()
        extended_user_form = RegistrationForm()


    return render(request, 'Registration/registration.html', {'user_form': user_form, 'extended_user_form': extended_user_form})
    # return render(request, 'Registration/registration.html',{'extended_user_form': extended_user_form})

@login_required(login_url='signIn')
def willowsfordWaiver(request):
    if request.method == "POST":
        user = User.objects.get(username=request.user, instance=user.useraccount)
        waiver_form = WillowsfordWaiverForm(request.POST)
        if waiver_form.is_valid():
            user = User.objects.get(username=request.user)
            waiver = waiver_form.save(commit=False)
            waiver.bday = user.useraccount.bday
            waiver.save()
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            print(waiver_form.errors)
            return render(request, 'Registration/willowsfordWaiver.html', {'waiver_form': waiver_form})
    else:
        waiver_form = WillowsfordWaiverForm()

    return render(request, 'Registration/willowsfordWaiver.html', {'waiver_form': waiver_form})

@login_required(login_url='signIn')
def archeryWaiver(request):
    if request.method == "POST":
        user = User.objects.get(username=request.user)
        waiver_form = ArcheryWaiverForm(request.POST, instance=user.useraccount)
        if waiver_form.is_valid():
            waiver = waiver_form.save(commit=False)
            waiver.bday = user.useraccount.bday #Form breaks for some reason if bday isnt there.
            waiver.save()
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            print(waiver_form.errors)
            return render(request, 'Registration/archeryWaiver.html.html', {'waiver_form': waiver_form})
    else:
        waiver_form = ArcheryWaiverForm()

    return render(request, 'Registration/archeryWaiver.html', {'waiver_form': waiver_form})

@login_required(login_url='signIn')
def rulesOfConductWaiver(request):
    if request.method == "POST":
        user = User.objects.get(username=request.user)
        waiver_form = RulesOfConductWaiverForm(request.POST, instance=user.useraccount)
        if waiver_form.is_valid():
            user = User.objects.get(username=request.user)
            waiver = waiver_form.save(commit=False)
            waiver.bday = user.useraccount.bday

            waiver.save()
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            print(waiver_form.errors)
            return render(request, 'Registration/rulesOfConductWaiver.html', {'waiver_form': waiver_form})
    else:
        waiver_form = RulesOfConductWaiverForm()

    return render(request, 'Registration/rulesOfConductWaiver.html', {'waiver_form': waiver_form})
