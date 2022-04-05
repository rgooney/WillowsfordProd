from django.db import models
from Registration.models import UserAccount
# Create your models here.
class Scores(models.Model):
    score_id = models.AutoField(primary_key=True)
    shooting_style = models.CharField(max_length=20)
    target_type = models.CharField(max_length=20)
    distance = models.IntegerField(max_length=20)
    num_arrows = models.IntegerField(max_length=20)
    score = models.IntegerField(max_length=20)
    time = models.TimeField(auto_now=True)
    date = models.DateField(auto_now=True)
    validator_approval = models.Boolean(default=False)
    account_id = models.ForeignKey(UserAccount, blank=True, null=True, on_delete=models.CASCADE)
