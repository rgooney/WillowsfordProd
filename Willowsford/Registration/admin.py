from django.contrib import admin
from .models import *
from MemberManagement.models import Statement
from datetime import datetime
import csv
from django.http import HttpResponse

# Register your models here.


class RegistrationAdmin(admin.ModelAdmin):
    actions = ["export_as_csv"]
    list_display = ('account_id', 'fname', 'lname', 'approved', 'membershipType', 'officer', 'most_recent_payment_date',
                    'most_recent_payment_amnt')
    search_fields = ['account_id', 'fname', 'lname']
    list_filter = ('membershipType', 'officer',)

    fieldsets = (
        (None, {
            'fields': ('user', 'fname', 'mid_initial', 'lname', 'gender', 'bday', 'approved', 'officer', 'membershipType')
        }),
        ('Contact Information', {
            'classes': ('collapse',),
            'fields': ('street', 'city', 'state', 'phonenumber')
        }),
        ('Waivers', {
            'classes': ('collapse',),
            'fields': ('willowsfordWaiverSigned', 'willowsfordWaiverSignedInitials', 'willowsfordWaiverSignedDate',
                       'archeryClubWaiverSigned', 'archeryClubWaiverSignedInitials', 'archeryClubWaiverSignedDate',
                       'rulesOfConductWaiverSigned', 'rulesOfConductWaiverSignedInitials', 'rulesOfConductWaiverSignedDate')
        }),
    )
    # Add columns for “Most Recent Payment Date” and “Most Recent Payment Amount”
    # to the Registration / User Account page.(DAVID)
    def most_recent_payment_date(self, obj):
        statements = Statement.objects.filter(account_id=obj.account_id).filter(paid=True)
        most_recent_statement_date = datetime.min.date()
        for i in statements:
            if i.paid_date > most_recent_statement_date:
                most_recent_statement_date = i.paid_date

        return most_recent_statement_date

    def most_recent_payment_amnt(self, obj):
        statements =  Statement.objects.filter(account_id=obj.account_id).filter(
            paid_date=self.most_recent_payment_date(obj))
        most_recent_payment_amnt = 0
        for i in statements:
            most_recent_payment_amnt = i.amount_paid

        return most_recent_payment_amnt

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected as CSV"

admin.site.register(UserAccount, RegistrationAdmin)

