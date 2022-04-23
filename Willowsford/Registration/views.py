from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .forms import *
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin

# Password Reset Imports
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

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
    else:
        user_form = UserAccountForm()
        extended_user_form = RegistrationForm()


    return render(request, 'Registration/registration.html', {'user_form': user_form, 'extended_user_form': extended_user_form})

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


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = 'Password Reset Requested'
                    email_template_name = 'password_reset_email.txt'
                    # The following needs to be corrected for WAC
                    c = {
                        "email":user.email,
                        'domain':'127.0.0.1:8000',
                        'site_name': 'Willowsford Archery Club',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        #The following needs to be registered to a real email
                        send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect ('/password_reset/done/')
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name='password_reset.html', context={'password_reset_form':password_reset_form})