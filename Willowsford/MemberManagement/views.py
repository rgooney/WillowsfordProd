from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db.models import Sum
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
import datetime
from django.utils import timezone

from .models import *
from .forms import *
from Scoring.models import *
from Registration.forms import *
from Registration.models import *

# Create your views here.
def signIn(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.useraccount.approved == True:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return HttpResponseRedirect(reverse('index'))
            elif user.useraccount.approved == False:
                messages.error(request, "Account is not yet approved. Please contact a club officer.")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm()

    return render(request, 'MemberManagement/signIn.html', {"form": form})

@login_required(login_url='signIn')
def dashboard(request):
    user = User.objects.get(username=request.user)
    guest_checkin_form = GuestCheckInForm()
    checkin_form = CheckInForm()

    ######################################
    # Balance calculations
    ######################################
    try:
        statement = Statement.objects.filter(account_id=user.useraccount).filter(paid=False).aggregate(tot_balance=Sum('amount_due'))
        total_balance = statement['tot_balance']
    except Statement.DoesNotExist:
        statement = None

    ######################################
    # Form field data for check-in
    ######################################
    if request.method == "POST" and "check_in" in request.POST:
        print("regular check in")
        checkin_form = CheckInForm(request.POST)
        if checkin_form.is_valid():
            checkin = checkin_form.save(commit=False)
            checkin.account_id = user.useraccount
            checkin.save()
            messages.success(request, "Successfully Checked In.")
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            print(checkin_form.errors)
            return render(request, 'MemberManagement/dashboard.html', {'total_balance': total_balance, 'checkin_form': checkin_form,
                                                                       'guest_checkin_form': guest_checkin_form})
    else:
        checkin_form = CheckInForm()

    #####################################
    # Form field data for guest check-in
    #####################################
    if request.method == "POST" and "guest_check_in" in request.POST:
        print("guest check in")
        guest_checkin_form = GuestCheckInForm(request.POST)
        if guest_checkin_form.is_valid():
            guest_checkin = guest_checkin_form.save(commit=False)
            guest_checkin.member_id = user.useraccount
            print("submitting")
            guest_checkin.save()
            messages.success(request, "Guest Successfully Checked In.")
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            print("Not submitting")
            print(guest_checkin_form.errors)
            return render(request, 'MemberManagement/dashboard.html', {'total_balance': total_balance, 'checkin_form': checkin_form,
                                                                       'guest_checkin_form': guest_checkin_form})
    else:
        guest_checkin_form = GuestCheckInForm()

    return render(request, 'MemberManagement/dashboard.html', {'total_balance': total_balance, 'checkin_form': checkin_form,
                                                               'guest_checkin_form': guest_checkin_form})

@login_required(login_url='signIn')
def statements(request):
    user = User.objects.get(username=request.user)
    try:
        check_ins = CheckIn.objects.filter(account_id=user.useraccount).filter(checkin_type='V')
        current_year = timezone.now().year
        volunteer_sum = 0
        for i in check_ins:
            if i.date > current_year:
                time = i.time_out.hour - i.time_in.hour
            volunteer_sum = volunteer_sum + time

        statements = Statement.objects.filter(account_id=user.useraccount).all()
        statement_total = Statement.objects.filter(account_id=user.useraccount).filter(paid=False).aggregate(tot_balance=Sum('amount_due'))
        total_balance = statement_total['tot_balance']
    except Statement.DoesNotExist:
        statement = None

    return render(request, 'MemberManagement/statements.html', {'statements': statements, 'total_balance': total_balance,
                                                                'current_year': current_year, 'volunteer_sum': volunteer_sum})

@login_required(login_url='signIn')
def scores(request):
    user = User.objects.get(username=request.user)
    try:
        scores = Scores.objects.filter(account_id=user.useraccount).all()
        maxValue = 0
        max = None

        for i in scores:
            if i.score >= maxValue:
                print('Current ID: ' + str(i.score_id))
                print('Current Score:' + str(i.score))
                print('Current Max:' + str(maxValue))
                maxValue = i.score
                max = i
    except Statement.DoesNotExist:
        scores = None

    return render(request, 'Scoring/viewScores.html', {'scores': scores, 'max': max}) #passing object

class PaypalReturnView(TemplateView):
    template_name = 'paypal_success.html'


class PaypalCancelView(TemplateView):
    template_name = 'paypal_cancel.html'
