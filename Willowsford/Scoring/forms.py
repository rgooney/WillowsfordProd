from xml.etree.ElementTree import Comment
from django import forms


class ManualScoringForm(forms.Form):
    #round 1
    r1n1 = forms.IntegerField()
    r1n2 = forms.IntegerField()
    r1n3 = forms.IntegerField()
    commentOne = forms.CharField()
    cum1 = 0
    sub1 = 0
    #round 2
    r2n1 = forms.IntegerField()
    r2n2 = forms.IntegerField()
    r2n3 = forms.IntegerField()
    commentTwo = forms.CharField()
    cum2 = 0
    sub2 = 0
    #round 3
    r3n1 = forms.IntegerField()
    r3n2 = forms.IntegerField()
    r3n3 = forms.IntegerField()
    commentThree = forms.CharField()
    cum3 = 0
    sub3 = 0
    #round 4
    r4n1 = forms.IntegerField()
    r4n2 = forms.IntegerField()
    r4n3 = forms.IntegerField()
    commentFour = forms.CharField()
    cum4 = 0
    sub4 = 0
    #round 5
    r5n1 = forms.IntegerField()
    r5n2 = forms.IntegerField()
    r5n3 = forms.IntegerField()
    commentFive = forms.CharField()
    cum5 = 0
    sub5 = 0
    #round 6
    r6n1 = forms.IntegerField()
    r6n2 = forms.IntegerField()
    r6n3 = forms.IntegerField()
    commentSix = forms.CharField()
    cum6 = 0
    sub6 = 0
    #round 7
    r7n1 = forms.IntegerField()
    r7n2 = forms.IntegerField()
    r7n3 = forms.IntegerField()
    commentSeven = forms.CharField()
    cum7 = 0 
    sub7 = 0
    #round 8
    r8n1 = forms.IntegerField()
    r8n2 = forms.IntegerField()
    r8n3 = forms.IntegerField()
    commentEight = forms.CharField()
    cum8 = 0 
    sub8 = 0
    #round 9 
    r9n1 = forms.IntegerField()
    r9n2 = forms.IntegerField()
    r9n3 = forms.IntegerField()
    commentNine = forms.CharField()
    cum9 = 0 
    sub9 = 0
    #round 10
    r10n1 = forms.IntegerField()
    r10n2 = forms.IntegerField()
    r10n3 = forms.IntegerField()
    commentTen = forms.CharField()
    cum10 = 0
    sub10 = 0
    result = 0
