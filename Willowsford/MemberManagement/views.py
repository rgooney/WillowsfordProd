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
        listOf10 = []
        listOf20 = []
        listOf30 = []
        listOf40 = []
        listOf60 = []
        listOfWillowsford = []

        for i in scores:
            if i.distance == "10 yards":
                listOf10.append(i)
            elif i.distance == "20 yards":
                listOf20.append(i)
            elif i.distance == "30 yards":
                listOf30.append(i)
            elif i.distance == "40 yards":
                listOf40.append(i)
            elif i.distance == "60 yards":
                listOf60.append(i)
            elif i.distance == "The Willowsford":
                listOfWillowsford.append(i)

        if listOf10[0] != None:
            max10 = listOf10[0]
        else:
            max10 = None
        if listOf20[0] != None:
            max20 = listOf20[0]
        else:
            max20 = None
        if listOf30[0] != None:
            max30 = listOf30[0]
        else:
            max30 = None
        if listOf40[0] != None:
            max40 = listOf40[0]
        else:
            max40 = None
        if listOf60[0] != None:
            max60 = listOf60[0]
        else:
            max60 = None
        if listOfWillowsford[0] != None:
            maxWillowsford = listOfWillowsford[0]
        else:
            maxWillowsford = None

        if max10 != None:
            for i in listOf10:
                if i.score >= max10.score:
                    max10 = i
        if max20 != None:
            for i in listOf20:
                if i.score >= max20.score:
                    max20 = i
        if max30 != None:
            for i in listOf30:
                if i.score >= max30.score:
                    max30 = i
        if max40 != None:
            for i in listOf40:
                if i.score >= max40.score:
                    max40 = i
        if max60 != None:
            for i in listOf60:
                if i.score >= max60.score:
                    max60 = i
        if maxWillowsford != None:
            for i in listOfWillowsford:
                if i.score >= maxWillowsford.score:
                    maxWillowsford = i

        print('The Max 10 init')
        print('Current ID: ' + str(max10.score_id))
        print('Current Score:' + str(max10.score))
        print('The Max 20 init')
        print('Current ID: ' + str(max20.score_id))
        print('Current Score:' + str(max20.score))
        print('The Max 30 init')
        print('Current ID: ' + str(max30.score_id))
        print('Current Score:' + str(max30.score))
        print('The Max 40 init')
        print('Current ID: ' + str(max40.score_id))
        print('Current Score:' + str(max40.score))
        print('The Max 60 init')
        print('Current ID: ' + str(max60.score_id))
        print('Current Score:' + str(max60.score))
        print('The Max Willowsford init')
        print('Current ID: ' + str(maxWillowsford.score_id))
        print('Current Score:' + str(maxWillowsford.score))

    except Statement.DoesNotExist:
        scores = None

    return render(request, 'Scoring/viewScores.html', {'scores': scores, 'max': max, 'max10': max10, 'max20': max20, 'max30': max30, 'max40': max40,
                                                       'max60': max60, 'maxWillowsford': maxWillowsford,}) #passing object

class PaypalReturnView(TemplateView):
    template_name = 'paypal_success.html'


class PaypalCancelView(TemplateView):
    template_name = 'paypal_cancel.html'
