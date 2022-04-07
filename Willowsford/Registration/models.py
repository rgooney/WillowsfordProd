from django.db import models
from django.contrib.auth.models import User


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

# Create your models here.
class UserAccount(models.Model):
    account_id = models.AutoField(max_length=10, primary_key=True)
    fname = models.CharField(max_length=30)
    mid_initial = models.CharField(max_length=2)
    lname = models.CharField(max_length=30)
    gender = models.CharField(max_length=10, choices=GENDER)
    bday = models.DateField()
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=30, default="Aldie")
    state = models.CharField(max_length=30, choices=STATES, default="Virginia")
    approved = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    officer = models.BooleanField(default=False)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.fname+' '+self.lname
