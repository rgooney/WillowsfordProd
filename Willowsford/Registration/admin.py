from django.contrib import admin
from .models import *

# Register your models here.


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('account_id','approved', 'fname', 'lname', 'street', 'city')

admin.site.register(UserAccount, RegistrationAdmin)

