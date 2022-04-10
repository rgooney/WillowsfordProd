from django.db import models
from Registration.models import UserAccount
from decimal import Decimal

# Create your models here.
MEMBER_CHOICES = (
    ('M', 'Member'),
    ('V', 'Volunteer'),
    ('O', 'Officer'),
    ('S', 'Willowsford Staff'),
)

class CheckIn(models.Model):
    checkin_id = models.AutoField(primary_key=True)
    date = models.DateField()
    time_in = models.TimeField()
    time_out = models.TimeField()
    checkin_type = models.CharField(max_length=20, choices=MEMBER_CHOICES)
    account_id = models.ForeignKey(UserAccount, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.checkin_id) + ": " + self.account_id.lname + " || " + str(self.date)

class Statement(models.Model):
    statement_id = models.AutoField(primary_key=True)
    bill_date = models.DateField()
    account_id = models.ForeignKey(UserAccount, blank=True, null=True, on_delete=models.CASCADE)
    amount_due = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return str(self.statement_id) + ": " + self.account_id.fname + self.account_id.lname