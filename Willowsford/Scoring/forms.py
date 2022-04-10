import email
from django import forms


#class RenewBookForm(forms.Form):
    #email = forms.EmailField()
    
class ManualScoringForm(forms.Form):
    #round 1
    r1n1 = forms.IntegerField()
    r1n2 = forms.IntegerField()
    r1n3 = forms.IntegerField()
    cum1 = 0
    #round 2
    r2n1 = forms.IntegerField()
    r2n2 = forms.IntegerField()
    r2n3 = forms.IntegerField()
    cum2 = 0
    #round 3
    r3n1 = forms.IntegerField()
    r3n2 = forms.IntegerField()
    r3n3 = forms.IntegerField()
    cum3 = 0
    #round 4
    r4n1 = forms.IntegerField()
    r4n2 = forms.IntegerField()
    r4n3 = forms.IntegerField()
    cum4 = 0
    #round 5
    r5n1 = forms.IntegerField()
    r5n2 = forms.IntegerField()
    r5n3 = forms.IntegerField()
    cum5 = 0
    #round 6
    r6n1 = forms.IntegerField()
    r6n2 = forms.IntegerField()
    r6n3 = forms.IntegerField()
    cum6 = 0
    #round 7
    r7n1 = forms.IntegerField()
    r7n2 = forms.IntegerField()
    r7n3 = forms.IntegerField()
    cum7 = 0 
    #round 8
    r8n1 = forms.IntegerField()
    r8n2 = forms.IntegerField()
    r8n3 = forms.IntegerField()
    cum8 = 0 
    #round 9 
    r9n1 = forms.IntegerField()
    r9n2 = forms.IntegerField()
    r9n3 = forms.IntegerField()
    cum9 = 0 
    #round 10
    r10n1 = forms.IntegerField()
    r10n2 = forms.IntegerField()
    r10n3 = forms.IntegerField()
    cum10 = 0
    result = 0
