from django.contrib import admin
from django.core.mail import send_mail
from .models import *

# Register your models here.


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('account_id','approved', 'fname', 'lname', 'street', 'city')
    list_editable = ('approved',)

admin.site.register(UserAccount, RegistrationAdmin)

