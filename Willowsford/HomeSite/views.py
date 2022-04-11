from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import RedirectView
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.urls import reverse
from Registration.models import *

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
    return render(request, 'HomeSite/services.html')


class SignOut(RedirectView):
    permanent = False
    query_string = True

    def get_redirect_url(self):
        logout(self.request)
        return reverse('index')


