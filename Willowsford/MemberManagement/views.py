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
                messages.error(request, "Account is not yet approved. Please contanct a club officer.")
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

    # Waiver Checks
    willowsford_renewal_check = False
    archery_renewal_check = False
    rules_of_conduct_renewal_check = False
    renewal_check_date = datetime.datetime.now() - datetime.timedelta(days=1*365)
    renewal_check_date = renewal_check_date.date()
    print('Waiver date: ' + str(request.user.useraccount.willowsfordWaiverSignedDate) + ' One year ago: ' + str(
        renewal_check_date))
    if renewal_check_date > request.user.useraccount.willowsfordWaiverSignedDate:
        willowsford_renewal_check = True
    elif renewal_check_date > request.user.useraccount.archeryClubWaiverSignedDate:
        archery_renewal_check = True
    elif renewal_check_date > request.user.useraccount.rulesOfConductWaiverSignedDate:
        rules_of_conduct_renewal_check = True

    # Balance calculations
    try:
        statement = Statement.objects.filter(account_id=user.useraccount).filter(paid=False).aggregate(tot_balance=Sum('amount_due'))
        total_balance = statement['tot_balance']
    except Statement.DoesNotExist:
        statement = None

    # Form field data for check-in
    if request.method == "POST":
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
                                                                       'willowsford_renewal_check': willowsford_renewal_check,
                                                                       'archery_renewal_check': archery_renewal_check,
                                                                       'rules_of_conduct_renewal_check': rules_of_conduct_renewal_check,})
    else:
        checkin_form = CheckInForm()

    return render(request, 'MemberManagement/dashboard.html', {'total_balance': total_balance, 'checkin_form': checkin_form,
                                                                       'willowsford_renewal_check': willowsford_renewal_check,
                                                                       'archery_renewal_check': archery_renewal_check,
                                                                       'rules_of_conduct_renewal_check': rules_of_conduct_renewal_check,})

@login_required(login_url='signIn')
def statements(request):
    user = User.objects.get(username=request.user)
    try:
        check_ins = CheckIn.objects.filter(account_id=user.useraccount).filter(checkin_type='V')
        waiver_date = user.useraccount.willowsfordWaiverSignedDate
        volunteer_sum = 0
        for i in check_ins:
            if i.date > waiver_date:
                time = i.time_out.hour - i.time_in.hour
            volunteer_sum = volunteer_sum + time

        statements = Statement.objects.filter(account_id=user.useraccount).all()
        statement_total = Statement.objects.filter(account_id=user.useraccount).filter(paid=False).aggregate(tot_balance=Sum('amount_due'))
        total_balance = statement_total['tot_balance']
    except Statement.DoesNotExist:
        statement = None

    return render(request, 'MemberManagement/statements.html', {'statements': statements, 'total_balance': total_balance,
                                                                'waiver_date': waiver_date, 'volunteer_sum': volunteer_sum})

@login_required(login_url='signIn')
def scores(request):
    user = User.objects.get(username=request.user)
    try:
        scores = Scores.objects.filter(account_id=user.useraccount).all()
        maxValue = 0
        for i in scores:
            #going thru each of the scores in users, for that user, referencing Scoring and models [score ' total score' ]
            # find max score, set a var to 0 and compare it to that, after - sitatuion w/ mult scores w/ same max value 
            #greater than or equal if i.score >= the last score that has the highest score record the last one it looks at 
            #last one it looks at should be max score 
            # just do it to point where u can print max score
            # dont do date time comparison
            # save into a variable and pass it back into the page, instead of print save into a var 
            if i.score >= maxValue:
                max = i #saving the whole object score id and date and everything
    except Statement.DoesNotExist:
        scores = None

    return render(request, 'Scoring/viewScores.html', {'scores': scores, 'max' : max}) #passing object 

class PaypalReturnView(TemplateView):
    template_name = 'paypal_success.html'


class PaypalCancelView(TemplateView):
    template_name = 'paypal_cancel.html'
