from django.contrib import admin
from .models import *

# Register your models here.


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('account_id', 'fname', 'lname', 'approved', 'membershipType', 'officer')
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
admin.site.register(UserAccount, RegistrationAdmin)

