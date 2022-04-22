from django.contrib import admin
from .models import *
import csv
from django.http import HttpResponse

# Register your models here.

class ScoringAdmin(admin.ModelAdmin):
    actions = ["export_as_csv"]
    list_display = ('score_id', 'account_id', 'datetime', 'validator_name', 'validator_approval', 'shooting_style' ,'distance', 'score')
    search_fields = ['score_id', 'account_id', 'datetime', 'validator_name']
    list_filter = ('validator_approval', 'shooting_style' ,'distance',)

    readonly_fields = ('cumulativeRoundOne', 'cumulativeRoundTwo', 'cumulativeRoundThree', 'cumulativeRoundFour',
                       'cumulativeRoundFive', 'cumulativeRoundSix', 'cumulativeRoundSeven', 'cumulativeRoundEight',
                       'cumulativeRoundNine', 'cumulativeRoundTen', 'subtotalRoundOne', 'subtotalRoundTwo',
                       'subtotalRoundThree', 'subtotalRoundFour', 'subtotalRoundFive', 'subtotalRoundSix',
                       'subtotalRoundSeven', 'subtotalRoundEight', 'subtotalRoundNine', 'subtotalRoundTen', 'score')
    fieldsets = (
        (None, {
            'fields': (
            'account_id', 'validator_name', 'validator_approval', 'datetime', 'shooting_style' ,'distance', 'score')
        }),
        ('Round 1', {
            'classes': ('collapse',),
            'fields': ('cumulativeRoundOne', 'subtotalRoundOne', 'commentRoundOne', 'r1n1', 'r1n2', 'r1n3')
        }),
        ('Round 2', {
            'classes': ('collapse',),
            'fields': ('cumulativeRoundTwo', 'subtotalRoundTwo', 'commentRoundTwo', 'r2n1', 'r2n2', 'r2n3')
        }),
        ('Round 3', {
            'classes': ('collapse',),
            'fields': ('cumulativeRoundThree', 'subtotalRoundThree', 'commentRoundThree', 'r3n1', 'r3n2', 'r3n3')
        }),
        ('Round 4', {
            'classes': ('collapse',),
            'fields': ('cumulativeRoundFour', 'subtotalRoundFour', 'commentRoundFour', 'r4n1', 'r4n2', 'r4n3')
        }),
        ('Round 5', {
            'classes': ('collapse',),
            'fields': ('cumulativeRoundFive', 'subtotalRoundFive', 'commentRoundFive', 'r5n1', 'r5n2', 'r5n3')
        }),
        ('Round 6', {
            'classes': ('collapse',),
            'fields': ('cumulativeRoundSix', 'subtotalRoundSix', 'commentRoundSix', 'r6n1', 'r6n2', 'r6n3')
        }),
        ('Round 7', {
            'classes': ('collapse',),
            'fields': ('cumulativeRoundSeven', 'subtotalRoundSeven', 'commentRoundSeven', 'r7n1', 'r7n2', 'r7n3')
        }),
        ('Round 8', {
            'classes': ('collapse',),
            'fields': ('cumulativeRoundEight', 'subtotalRoundEight', 'commentRoundEight', 'r8n1', 'r8n2', 'r8n3')
        }),
        ('Round 9', {
            'classes': ('collapse',),
            'fields': ('cumulativeRoundNine', 'subtotalRoundNine', 'commentRoundNine', 'r9n1', 'r9n2', 'r9n3')
        }),
        ('Round 10', {
            'classes': ('collapse',),
            'fields': ('cumulativeRoundTen', 'subtotalRoundTen', 'commentRoundTen', 'r10n1', 'r10n2', 'r10n3')
        }),

    )

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

admin.site.register(Scores, ScoringAdmin)