from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.CheckIn)
admin.site.register(models.Statement)

# list displays don't work because its multiple models
#

class CheckInAdmin(admin.ModelAdmin):
    list_display= ('checkin_id','date','checkin_type')


class StatementAdmin(models.ModelAmin):
    list_display = ('statement_id','bill_date', 'amount_due')
