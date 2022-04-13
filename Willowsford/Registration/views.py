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
            print(user_form.errors)
            print(extended_user_form.errors)
            return render(request, 'Registration/registration.html',
                          {'user_form': user_form, 'extended_user_form': extended_user_form})
    else:
        user_form = UserAccountForm()
        extended_user_form = RegistrationForm()


    return render(request, 'Registration/registration.html', {'user_form': user_form, 'extended_user_form': extended_user_form})

def willowsfordWaiver(request):
    if request.method == "POST":
        waiver_form = WillowsfordWaiverForm(request.POST)
        if waiver_form.is_valid():
            user = User.objects.get(username=request.user)
            user.willowsfordWaiverSigned = waiver_form.fields['willowsfordWaiverSigned']
            user.willowsfordWaiverSignedInitials = waiver_form.fields['willowsfordWaiverSignedInitials']
            user.willowsfordWaiverSignedDate = waiver_form.fields['willowsfordWaiverSignedDate']
            user.save()
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            print(waiver_form.errors)
            return render(request, 'Registration/willowsfordWaiver.html', {'waiver_form': waiver_form})
    else:
        waiver_form = WillowsfordWaiverForm()

    return render(request, 'Registration/willowsfordWaiver.html', {'waiver_form': waiver_form})

def archeryWaiver(request):
    if request.method == "POST":
        waiver_form = ArcheryWaiverForm(request.POST)
        if waiver_form.is_valid():
            user = User.objects.get(username=request.user)
            user.useraccount.archeryClubWaiverSigned = waiver_form.fields['archeryClubWaiverSigned']
            user.useraccount.archeryClubWaiverSignedInitials = waiver_form.fields['archeryClubWaiverSignedInitials']
            user.useraccount.archeryClubWaiverSignedDate = waiver_form.fields['archeryClubWaiverSignedDate']
            user.useraccount.save()
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            print(waiver_form.errors)
            return render(request, 'Registration/archeryWaiver.html.html', {'waiver_form': waiver_form})
    else:
        waiver_form = ArcheryWaiverForm()

    return render(request, 'Registration/archeryWaiver.html', {'waiver_form': waiver_form})


def rulesOfConductWaiver(request):
    if request.method == "POST":
        waiver_form = RulesOfConductWaiverForm(request.POST)
        if waiver_form.is_valid():
            user = waiver_form.save(commit=False)
            user.save()
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            print(waiver_form.errors)
            return render(request, 'Registration/rulesOfConductWaiver.html', {'waiver_form': waiver_form})
    else:
        waiver_form = RulesOfConductWaiverForm()

    return render(request, 'Registration/rulesOfConductWaiver.html', {'waiver_form': waiver_form})
