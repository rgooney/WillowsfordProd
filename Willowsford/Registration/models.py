from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
import datetime

STATES = (("Alabama","Alabama"),("Alaska","Alaska"),("Arizona","Arizona"),("Arkansas","Arkansas"),
          ("California","California"),("Colorado","Colorado"),("Connecticut","Connecticut"),
          ("Delaware","Delaware"),("Florida","Florida"),("Georgia","Georgia"),("Hawaii","Hawaii"),
          ("Idaho","Idaho"),("Illinois","Illinois"),("Indiana","Indiana"),("Iowa","Iowa"),("Kansas","Kansas"),
          ("Kentucky","Kentucky"),("Louisiana","Louisiana"),("Maine","Maine"),("Maryland","Maryland"),
          ("Massachusetts","Massachusetts"),("Michigan","Michigan"),("Minnesota","Minnesota"),
          ("Mississippi","Mississippi"),("Missouri","Missouri"),("Montana","Montana"),("Nebraska","Nebraska"),
          ("Nevada","Nevada"),("New Hampshire","New Hampshire"),("New Jersey","New Jersey"),("New Mexico","New Mexico"),
          ("New York","New York"),("North Carolina","North Carolina"),("North Dakota","North Dakota"),("Ohio","Ohio"),
          ("Oklahoma","Oklahoma"),("Oregon","Oregon"),("Pennsylvania","Pennsylvania"),("Rhode Island","Rhode Island"),
          ("South Carolina","South Carolina"),("South Dakota","South Dakota"),("Tennessee","Tennessee"),
          ("Texas","Texas"),("Utah","Utah"),("Vermont","Vermont"),("Virginia","Virginia"),("Washington","Washington"),
          ("West Virginia","West Virginia"),("Wisconsin","Wisconsin"),("Wyoming", "Wyoming"))

GENDER = (("Male", "Male"), ("Female", "Female"), ("Other", "Other"))

MEMBERSHIP_TYPE = (("Individual", "Individual"), ("Household", "Household"))

# Create your models here.
class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    account_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=30)
    mid_initial = models.CharField(max_length=2)
    lname = models.CharField(max_length=30)
    gender = models.CharField(max_length=10, choices=GENDER)
    bday = models.DateField()
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=30, default="Aldie")
    state = models.CharField(max_length=30, choices=STATES, default="Virginia")
    approved = models.BooleanField(default=False)
    membershipType = models.CharField(max_length=30, choices=MEMBERSHIP_TYPE, default="Individual")
    admin = models.BooleanField(default=False)
    officer = models.BooleanField(default=False)
    phonenumber = PhoneNumberField(blank=True)

    willowsfordWaiverSigned = models.BooleanField(default=False)
    willowsfordWaiverSignedInitials = models.CharField(blank=True, null=True, max_length=5)
    willowsfordWaiverSignedDate = models.DateField(blank=True, null=True, default=datetime.date.today)
    archeryClubWaiverSigned = models.BooleanField(default=False)
    archeryClubWaiverSignedInitials = models.CharField(blank=True, null=True, max_length=5)
    archeryClubWaiverSignedDate = models.DateField(blank=True, null=True, default=datetime.date.today)
    rulesOfConductWaiverSigned = models.BooleanField(default=False)
    rulesOfConductWaiverSignedInitials = models.CharField(blank=True, null=True, max_length=5)
    rulesOfConductWaiverSignedDate = models.DateField(blank=True, null=True, default=datetime.date.today)

    def __str__(self):
        return self.fname + " " + self.lname
