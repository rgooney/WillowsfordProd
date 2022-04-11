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
            "bday": forms.DateInput(),
        }
