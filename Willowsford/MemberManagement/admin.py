from django import forms
from django.contrib import admin
from decimal import Decimal
from . import models
from Registration.models import UserAccount

class CheckInAdmin(admin.ModelAdmin):
    list_display= ('checkin_id', 'account_id', 'date','checkin_type', 'time_in', 'time_out')
    search_fields = ['checkin_id', 'account_id', 'date', 'checkin_type']
    list_filter = ('checkin_type',)

class StatementAdminForm(forms.ModelForm):
    class Meta:
        model = models.Statement
        fields = ('statement_id', 'account_id', 'bill_date', 'amount_due', 'paid')

class StatementAdmin(admin.ModelAdmin):
    readonly_fields = ('volunteer_hours', 'last_membership_date')
    fields = ('account_id', 'bill_date', 'amount_due', 'paid', 'volunteer_hours', 'last_membership_date')
    list_display = ('statement_id', 'account_id', 'bill_date', 'amount_due', 'paid')
    search_fields = ['statement_id', 'account_id', 'bill_date', 'amount_due', 'paid']
    list_filter = ('paid',)

    # Calculates volunteer hours since the last time a membership has been renewed
    def volunteer_hours(self, obj):
        # Get all check-ins
        check_ins = models.CheckIn.objects.filter(account_id=obj.account_id).filter(checkin_type='V')
        waiver_date = obj.account_id.willowsfordWaiverSignedDate
        volunteer_sum = 0
        for i in check_ins:
            if i.date > waiver_date:
                time = i.time_out.hour - i.time_in.hour
            volunteer_sum = volunteer_sum + time

        return volunteer_sum

    def last_membership_date(self, obj):
        return obj.account_id.willowsfordWaiverSignedDate


# Register your models here.
admin.site.register(models.CheckIn, CheckInAdmin)
admin.site.register(models.Statement, StatementAdmin)