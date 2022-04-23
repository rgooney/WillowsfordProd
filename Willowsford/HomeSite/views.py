from django.views.generic.base import RedirectView
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.urls import reverse
from Registration.models import *
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        try:
            user = User.objects.get(username=request.user.username)
            account_name = user.useraccount.fname
        except UserAccount.DoesNotExist:
            account = None

    return render(request, 'HomeSite/index.html')


def about(request):
    return render(request, 'HomeSite/about.html')


def services(request):
    if request.method == 'GET':
        form = emailForm()
    else:
        form = emailForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                message += '\nThis email is from '
                message += name
                message += " at "
                message += from_email
                subject = 'questions from '
                subject += name
                send_mail(subject, message, from_email, ['rachel.gooney@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('response')
    return render(request, 'HomeSite/services.html', {'form': form})

def responseView(request):
    return render(request, 'HomeSite/questionResponse.html')

class SignOut(RedirectView):
    permanent = False
    query_string = True

    def get_redirect_url(self):
        logout(self.request)
        return reverse('index')



