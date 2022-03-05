from django.db import models

# Create your models here.
class UserAccount(models.Model):
    account_id = models.AutoField(max_length=10, primary_key=True)
    fname = models.CharField(max_length=30)
    mid_initial = models.CharField(max_length=2)
    lname = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    bday = models.DateField()
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    admin = models.BooleanField()
    officer = models.BooleanField()

    # TODO: Add waiver fields, and user/password