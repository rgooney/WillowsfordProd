from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

from .models import *

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = [


        ]

