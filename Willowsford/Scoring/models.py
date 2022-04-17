from django.db import models
from Registration.models import UserAccount
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
STYLES = (
            ('R/L w/o S','Recurve or longbow with no sights.  Finger release only - no mechanical release.'),
            ('R/L w/ S','Recurve or longbow with sights.  Finger release only - no mechanical release.'),
            ('R/L w/ S_and_M','Recurve or longbow with sights and mechanical release.' ),
            ('Compound','Compound bow, standing with no external rest' ))

DISTANCE = (('The Willowsford', 'The Willowsford'),
            ('10 yards', '10 yards'),
            ('10 yards', '20 yards'),
            ('10 yards', '30 yards'),
            ('10 yards', '40 yards'),
            ('10 yards', '50 yards'))

class Scores(models.Model):
    score_id = models.AutoField(primary_key=True)
    shooting_style = models.CharField(max_length=20, choices=STYLES, default='R/L w/o S')
    distance = models.CharField(max_length=20, choices=DISTANCE, default='The Willowsford')
    score = models.IntegerField("Total score", default=0,validators=[MaxValueValidator(200),MinValueValidator(0)])
    datetime = models.DateTimeField("Date")
    validator_name = models.CharField(max_length=20, blank=True, null=True)
    validator_approval = models.BooleanField(default=False)
    account_id = models.ForeignKey(UserAccount, blank=True, null=True, on_delete=models.CASCADE)

    r1n1 = models.IntegerField(default=0,validators=[MaxValueValidator(5),MinValueValidator(0)])
    r1n2 = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    r1n3 = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    commentRoundOne = models.CharField(null=True, blank=True, max_length=50)
    cumulativeRoundOne = models.IntegerField(default=0)
    subtotalRoundOne = models.IntegerField(default=0)

    r2n1 = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    r2n2 = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    r2n3 = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    commentRoundTwo = models.CharField(null=True, blank=True, max_length=50)
    cumulativeRoundTwo = models.IntegerField(default=0)
    subtotalRoundTwo = models.IntegerField(default=0)

    r3n1 = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    r3n2 = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    r3n3 = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    commentRoundThree = models.CharField(null=True, blank=True, max_length=50)
    cumulativeRoundThree = models.IntegerField(default=0)
    subtotalRoundThree = models.IntegerField(default=0)

    r4n1 = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    r4n2 = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    r4n3 = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    commentRoundFour = models.CharField(null=True, blank=True, max_length=50)
    cumulativeRoundFour = models.IntegerField(default=0)
    subtotalRoundFour = models.IntegerField(default=0)

    r5n1 = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    r5n2 = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    r5n3 = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    commentRoundFive = models.CharField(null=True, blank=True, max_length=50)
    cumulativeRoundFive = models.IntegerField(default=0)
    subtotalRoundFive = models.IntegerField(default=0)

    r6n1 = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    r6n2 = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    r6n3 = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    commentRoundSix = models.CharField(null=True, blank=True, max_length=50)
    cumulativeRoundSix = models.IntegerField(default=0)
    subtotalRoundSix = models.IntegerField(default=0)

    r7n1 = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    r7n2 = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    r7n3 = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    commentRoundSeven = models.CharField(null=True, blank=True, max_length=50)
    cumulativeRoundSeven = models.IntegerField(default=0)
    subtotalRoundSeven = models.IntegerField(default=0)

    r8n1 = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    r8n2 = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    r8n3 = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    commentRoundEight = models.CharField(null=True, blank=True, max_length=50)
    cumulativeRoundEight = models.IntegerField(default=0)
    subtotalRoundEight = models.IntegerField(default=0)

    r9n1 = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    r9n2 = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    r9n3 = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    commentRoundNine = models.CharField(null=True, blank=True, max_length=50)
    cumulativeRoundNine = models.IntegerField(default=0)
    subtotalRoundNine = models.IntegerField(default=0)

    r10n1 = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    r10n2 = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    r10n3 = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    commentRoundTen = models.CharField(null=True, blank=True, max_length=50)
    cumulativeRoundTen = models.IntegerField(default=0)
    subtotalRoundTen = models.IntegerField(default=0)
