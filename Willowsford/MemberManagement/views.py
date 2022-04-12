from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db.models import Sum

from .models import *
from django.views.generic import TemplateView
from Registration.models import *

# Create your views here.
def signIn(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return HttpResponseRedirect(reverse('index'))
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm()

    return render(request, 'MemberManagement/signIn.html', {"form": form})


def dashboard(request):
    user = User.objects.get(username=request.user)
    print (user.useraccount.fname)
    try:
        statement = Statement.objects.filter(account_id=user.useraccount).filter(paid=False).aggregate(tot_balance=Sum('amount_due'))
        total_balance = statement['tot_balance']
    except Statement.DoesNotExist:
        statement = None

    return render(request, 'MemberManagement/dashboard.html', {'total_balance': total_balance})

def statements(request):
    user = User.objects.get(username=request.user)
    try:
        statements = Statement.objects.filter(account_id=user.useraccount).all()
        statement_total = Statement.objects.filter(account_id=user.useraccount).filter(paid=False).aggregate(tot_balance=Sum('amount_due'))
        total_balance = statement_total['tot_balance']
    except Statement.DoesNotExist:
        statement = None

    return render(request, 'MemberManagement/statements.html', {'statements': statements, 'total_balance': total_balance})

class PaypalReturnView(TemplateView):
    template_name = 'paypal_success.html'


class PaypalCancelView(TemplateView):
    template_name = 'paypal_cancel.html'
