from xml.etree.ElementTree import Comment
from django import forms


class ManualScoringForm(forms.Form):
    #round 1
    r1n1 = forms.IntegerField(initial=0)
    r1n2 = forms.IntegerField(initial=0)
    r1n3 = forms.IntegerField(initial=0)
    commentOne = forms.CharField(required = False)
    cum1 = 0
    sub1 = 0
    #round 2
    r2n1 = forms.IntegerField(initial=0)
    r2n2 = forms.IntegerField(initial=0)
    r2n3 = forms.IntegerField(initial=0)
    commentTwo = forms.CharField(required = False)
    cum2 = 0
    sub2 = 0
    #round 3
    r3n1 = forms.IntegerField(initial=0)
    r3n2 = forms.IntegerField(initial=0)
    r3n3 = forms.IntegerField(initial=0)
    commentThree = forms.CharField(required = False)
    cum3 = 0
    sub3 = 0
    #round 4
    r4n1 = forms.IntegerField(initial=0)
    r4n2 = forms.IntegerField(initial=0)
    r4n3 = forms.IntegerField(initial=0)
    commentFour = forms.CharField(required = False)
    cum4 = 0
    sub4 = 0
    #round 5
    r5n1 = forms.IntegerField(initial=0)
    r5n2 = forms.IntegerField(initial=0)
    r5n3 = forms.IntegerField(initial=0)
    commentFive = forms.CharField(required = False)
    cum5 = 0
    sub5 = 0
    #round 6
    r6n1 = forms.IntegerField(initial=0)
    r6n2 = forms.IntegerField(initial=0)
    r6n3 = forms.IntegerField(initial=0)
    commentSix = forms.CharField(required = False)
    cum6 = 0
    sub6 = 0
    #round 7
    r7n1 = forms.IntegerField(initial=0)
    r7n2 = forms.IntegerField(initial=0)
    r7n3 = forms.IntegerField(initial=0)
    commentSeven = forms.CharField(required = False)
    cum7 = 0 
    sub7 = 0
    #round 8
    r8n1 = forms.IntegerField(initial=0)
    r8n2 = forms.IntegerField(initial=0)
    r8n3 = forms.IntegerField(initial=0)
    commentEight = forms.CharField(required = False)
    cum8 = 0 
    sub8 = 0
    #round 9 
    r9n1 = forms.IntegerField(initial=0)
    r9n2 = forms.IntegerField(initial=0)
    r9n3 = forms.IntegerField(initial=0)
    commentNine = forms.CharField(required = False)
    cum9 = 0 
    sub9 = 0
    #round 10
    r10n1 = forms.IntegerField(initial=0)
    r10n2 = forms.IntegerField(initial=0)
    r10n3 = forms.IntegerField(initial=0)
    commentTen = forms.CharField(required = False)
    cum10 = 0
    sub10 = 0
    result = 0
