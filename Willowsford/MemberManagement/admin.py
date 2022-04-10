from django import forms
from django.contrib import admin
from decimal import Decimal
from . import models

class CheckInAdmin(admin.ModelAdmin):
    list_display= ('checkin_id','date','checkin_type')

class StatementForm(forms.ModelForm):
    class Meta:
        model = models.Statement
        fields = ['account_id', 'bill_date', 'amount_due']

        amount_due = forms.DecimalField(initial=10.00)

class StatementAdmin(admin.ModelAdmin):
    list_display = ('statement_id', 'bill_date', 'amount_due')
    # form = StatementForm(initial={'amount_due': Decimal(10.00)})
    # form.base_fields['amount_due'].initial = Decimal(10.00)

    # def get_changeform_initial_data(self, request):
    #     return {'amount_due': Decimal(10.00)}


    # def get_form(self, request, obj=None, **kwargs):
    #     form = super(StatementAdmin, self).get_form(request, obj, **kwargs)
    #     form.base_fields['amount_due'].initial = 10.00
    #     return form

# Register your models here.
admin.site.register(models.CheckIn, CheckInAdmin)
admin.site.register(models.Statement, StatementAdmin)