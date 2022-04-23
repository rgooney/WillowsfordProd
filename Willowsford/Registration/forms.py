from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import datetime

from .models import *
from phonenumber_field.formfields import *

year = datetime.datetime.now().date().strftime("%Y")

class UserAccountForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class RegistrationForm(forms.ModelForm):
    phonenumber = PhoneNumberField(widget=forms.TextInput(attrs={'onkeydown':'phoneNumberFormatter()'}))

    class Meta:
        model = UserAccount
        fields = ("fname", "mid_initial", "lname", "gender", "bday", "street", "city", "state", "membershipType", "phonenumber", "user", "zip")


        widgets = {
            "bday": forms.DateInput(attrs={'type': 'date'}),
        }

class GuestRegistrationForm(forms.ModelForm):

    class Meta:
        model = Guests
        fields = ("fname", "mid_initial", "lname", "gender", "bday", "willowsfordWaiver", "archeryClubWaiver", "rulesOfConductWaiver")


        widgets = {
            "bday": forms.DateInput(attrs={'type': 'date'}),
        }


class WillowsfordWaiverForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ["willowsfordWaiver"]


class ArcheryWaiverForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ["archeryClubWaiver", "archeryClubWaiverSigned"]


class RulesOfConductWaiverForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ["rulesOfConductWaiver", "archeryClubWaiverSigned"]
