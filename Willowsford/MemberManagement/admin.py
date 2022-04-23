from django import forms
from django.contrib import admin
from decimal import Decimal
from . import models
from django.utils import timezone
from Registration.models import UserAccount
import csv
from django.http import HttpResponse

class CheckInAdmin(admin.ModelAdmin):
    actions = ["export_as_csv"]
    list_display= ('checkin_id', 'account_id', 'date','checkin_type', 'time_in', 'time_out')
    search_fields = ['checkin_id', 'account_id', 'date', 'checkin_type']
    list_filter = ('checkin_type',)

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

class GuestCheckInAdmin(admin.ModelAdmin):
    actions = ["export_as_csv"]
    list_display= ('checkin_id', 'guest_id', 'member_id', 'date', 'time_in',)
    search_fields = ['checkin_id', 'guest_id', 'member_id', 'date', 'time_in',]

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

class StatementAdmin(admin.ModelAdmin):
    actions = ["export_as_csv"]
    readonly_fields = ('volunteer_hours', 'current_year')
    fields = ('account_id', 'bill_date', 'due_date', 'amount_due', 'paid', 'amount_paid', 'paid_date', 'volunteer_hours', 'current_year')
    list_display = ('statement_id', 'account_id', 'bill_date', 'amount_due', 'paid', 'paid_date')
    search_fields = ['statement_id', 'account_id', 'bill_date', 'amount_due', 'paid']
    list_filter = ('paid',)

    # Calculates volunteer hours since the last time a membership has been renewed
    def volunteer_hours(self, obj):
        # Get all check-ins
        check_ins = models.CheckIn.objects.filter(account_id=obj.account_id).filter(checkin_type='V')
        current_year = timezone.now().year
        volunteer_sum = 0
        for i in check_ins:
            if i.date > current_year:
                time = i.time_out.hour - i.time_in.hour
            volunteer_sum = volunteer_sum + time

        return volunteer_sum

    def current_year(self, obj):
        return timezone.now().year

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

# Register your models here.
admin.site.register(models.CheckIn, CheckInAdmin)
admin.site.register(models.Statement, StatementAdmin)
admin.site.register(models.GuestCheckIn, GuestCheckInAdmin)