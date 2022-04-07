from django import forms

class ManualScoringForm(forms.Form):
    r1n1 = forms.IntegerField()
    r1n2 = forms.IntegerField()
    r1n3 = forms.IntegerField()
    result = 0
