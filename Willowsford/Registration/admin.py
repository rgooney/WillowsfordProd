from django.contrib import admin
from .models import *

# Register your models here.


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('account_id', 'username', 'fname', 'lname', 'approved', 'officer', 'admin')

admin.site.register(UserAccount, RegistrationAdmin)