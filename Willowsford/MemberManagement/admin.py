from django import forms
from django.contrib import admin
from decimal import Decimal
from . import models

class CheckInAdmin(admin.ModelAdmin):
    list_display= ('checkin_id', 'account_id', 'date','checkin_type')

class StatementAdmin(admin.ModelAdmin):
    list_display = ('statement_id', 'account_id', 'bill_date', 'amount_due', 'paid')

# Register your models here.
admin.site.register(models.CheckIn, CheckInAdmin)
admin.site.register(models.Statement, StatementAdmin)