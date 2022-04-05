from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


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
    return render(request, 'MemberManagement/dashboard.html')





# noinspection PyInterpreter
def adminPanel(request):
    # verify that user is an admin
    return render(request, 'MemberManagement/adminPanel.html')