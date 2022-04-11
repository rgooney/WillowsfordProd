from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import datetime

from .models import *

year = datetime.datetime.now().date().strftime("%Y")

class UserAccountForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ("fname", "mid_initial", "lname", "gender", "bday", "street", "city", "state", "membershipType")

        widgets = {
            "bday": forms.SelectDateWidget(),
        }

    def clean_street(self):
        print("Clean Street method Called ... ")
        street_info = self.cleaned_data.get("street")
        print("Clean Street method Called ... ", street_info)
        return street_info

    def clean(self):
        print ("Clean method on ContactForm called")

        city = self.cleaned_data.get("city")
        zip = self.cleaned_data.get("zip")
        if (city == "Reston" and zip != "20168"):
            self.add_error("", "Invalid City and Zip code combination entered")

