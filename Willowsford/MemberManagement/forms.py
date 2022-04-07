from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from Registration import UserAccount

class ApprovalForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ("approved")

