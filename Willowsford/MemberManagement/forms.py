from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from django.views.generic import FormView
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from .models import Statement, CheckIn
from Registration.models import UserAccount

class PaypalFormView(FormView):
    template_name = 'paypal_form.html'
    form_class = PayPalPaymentsForm

    def get_initial(self):
        return {
            "business": '[email protected]',
            "amount": 20,
            "currency_code": "USD",
            "item_name": 'Member Dues',
            "invoice": 1234,    # Change to Statement.invoice_id
            "notify_url": self.request.build_absolute_uri(reverse('paypal-ipn')),
            "return_url": self.request.build_absolute_uri(reverse('paypal-return')),
            "cancel_return": self.request.build_absolute_uri(reverse('paypal-cancel')),
            "lc": 'US',
            "no_shipping": '1',
        }

class CheckInForm(forms.ModelForm):
    class Meta:
        model = CheckIn
        fields = ["date", "time_in","time_out","checkin_type", "account_id"]

        widgets = {
            "time_in": forms.TimeInput(),
            "time_out": forms.TimeInput(),
        }