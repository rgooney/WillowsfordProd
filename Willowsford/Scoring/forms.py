from xml.etree.ElementTree import Comment
from django import forms
from .models import Scores

# class ManualScoringForm(forms.Form):
#     #round 1
#     r1n1 = forms.IntegerField(initial=0)
#     r1n2 = forms.IntegerField(initial=0)
#     r1n3 = forms.IntegerField(initial=0)
#     commentOne = forms.CharField(required=False)
#     cumulative1 = forms.IntegerField(initial=0, disabled=True)
#     subtotal1 = forms.IntegerField(initial=0, disabled=True)
#     #round 2
#     r2n1 = forms.IntegerField(initial=0)
#     r2n2 = forms.IntegerField(initial=0)
#     r2n3 = forms.IntegerField(initial=0)
#     commentTwo = forms.CharField(required = False)
#     cumulative2 = forms.IntegerField(initial=0)
#     subtotal2 = forms.IntegerField(initial=0)
#     #round 3
#     r3n1 = forms.IntegerField(initial=0)
#     r3n2 = forms.IntegerField(initial=0)
#     r3n3 = forms.IntegerField(initial=0)
#     commentThree = forms.CharField(required = False)
#     cumulative3 = 0
#     sub3 = 0
#     #round 4
#     r4n1 = forms.IntegerField(initial=0)
#     r4n2 = forms.IntegerField(initial=0)
#     r4n3 = forms.IntegerField(initial=0)
#     commentFour = forms.CharField(required = False)
#     cumulative4 = 0
#     sub4 = 0
#     #round 5
#     r5n1 = forms.IntegerField(initial=0)
#     r5n2 = forms.IntegerField(initial=0)
#     r5n3 = forms.IntegerField(initial=0)
#     commentFive = forms.CharField(required = False)
#     cumulative5 = 0
#     sub5 = 0
#     #round 6
#     r6n1 = forms.IntegerField(initial=0)
#     r6n2 = forms.IntegerField(initial=0)
#     r6n3 = forms.IntegerField(initial=0)
#     commentSix = forms.CharField(required = False)
#     cumulative6 = 0
#     sub6 = 0
#     #round 7
#     r7n1 = forms.IntegerField(initial=0)
#     r7n2 = forms.IntegerField(initial=0)
#     r7n3 = forms.IntegerField(initial=0)
#     commentSeven = forms.CharField(required = False)
#     cumulative7 = 0
#     sub7 = 0
#     #round 8
#     r8n1 = forms.IntegerField(initial=0)
#     r8n2 = forms.IntegerField(initial=0)
#     r8n3 = forms.IntegerField(initial=0)
#     commentEight = forms.CharField(required = False)
#     cumulative8 = 0
#     sub8 = 0
#     #round 9
#     r9n1 = forms.IntegerField(initial=0)
#     r9n2 = forms.IntegerField(initial=0)
#     r9n3 = forms.IntegerField(initial=0)
#     commentNine = forms.CharField(required = False)
#     cumulative9 = 0
#     sub9 = 0
#     #round 10
#     r10n1 = forms.IntegerField(initial=0)
#     r10n2 = forms.IntegerField(initial=0)
#     r10n3 = forms.IntegerField(initial=0)
#     commentTen = forms.CharField(required = False)
#     cumulative10 = 0
#     sub10 = 0
#     result = 0

class ManualScoringModelForm(forms.ModelForm):
    class Meta:
        model = Scores
        fields = (
            "shooting_style", "distance", "score", "datetime",
            "r1n1", "r1n2", "r1n3", "commentRoundOne", "cumulativeRoundOne", "subtotalRoundOne",
            "r2n1", "r2n2", "r2n3", "commentRoundTwo", "cumulativeRoundTwo", "subtotalRoundTwo",
            "r3n1", "r3n2", "r3n3", "commentRoundThree", "cumulativeRoundThree", "subtotalRoundThree",
            "r4n1", "r4n2", "r4n3", "commentRoundFour", "cumulativeRoundFour", "subtotalRoundFour",
            "r5n1", "r5n2", "r5n3", "commentRoundFive", "cumulativeRoundFive", "subtotalRoundFive",
            "r6n1", "r6n2", "r6n3", "commentRoundSix", "cumulativeRoundSix", "subtotalRoundSix",
            "r7n1", "r7n2", "r7n3", "commentRoundSeven", "cumulativeRoundSeven", "subtotalRoundSeven",
            "r8n1", "r8n2", "r8n3", "commentRoundEight", "cumulativeRoundEight", "subtotalRoundEight",
            "r9n1", "r9n2", "r9n3", "commentRoundNine", "cumulativeRoundNine", "subtotalRoundNine",
            "r10n1", "r10n2", "r10n3", "commentRoundTen", "cumulativeRoundTen", "subtotalRoundTen",
        )

        widgets = {
            "shooting_style": forms.RadioSelect(),
            "datetime": forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            "subtotalRoundOne": forms.NumberInput(attrs={'style': 'background-color: #CDCDCD;'}),
            "cumulativeRoundOne" : forms.NumberInput(attrs={'style':'background-color: #CDCDCD;'}),
            "subtotalRoundTwo": forms.NumberInput(attrs={'readonly': 'readonly', 'style': 'background-color: #CDCDCD;'}),
            "cumulativeRoundTwo": forms.NumberInput(attrs={'readonly': 'readonly', 'style': 'background-color: #CDCDCD;'}),
            "subtotalRoundThree": forms.NumberInput(attrs={'readonly': 'readonly', 'style': 'background-color: #CDCDCD;'}),
            "cumulativeRoundThree": forms.NumberInput(attrs={'readonly': 'readonly', 'style': 'background-color: #CDCDCD;'}),
            "subtotalRoundFour": forms.NumberInput(attrs={'readonly': 'readonly', 'style': 'background-color: #CDCDCD;'}),
            "cumulativeRoundFour": forms.NumberInput(attrs={'readonly': 'readonly', 'style': 'background-color: #CDCDCD;'}),
            "subtotalRoundFive": forms.NumberInput(attrs={'readonly': 'readonly', 'style': 'background-color: #CDCDCD;'}),
            "cumulativeRoundFive": forms.NumberInput(attrs={'readonly': 'readonly', 'style': 'background-color: #CDCDCD;'}),
            "subtotalRoundSix": forms.NumberInput(attrs={'readonly': 'readonly', 'style': 'background-color: #CDCDCD;'}),
            "cumulativeRoundSix": forms.NumberInput(attrs={'readonly': 'readonly', 'style': 'background-color: #CDCDCD;'}),
            "subtotalRoundSeven": forms.NumberInput(attrs={'readonly': 'readonly', 'style': 'background-color: #CDCDCD;'}),
            "cumulativeRoundSeven": forms.NumberInput(attrs={'readonly': 'readonly', 'style': 'background-color: #CDCDCD;'}),
            "subtotalRoundEight": forms.NumberInput(attrs={'readonly': 'readonly', 'style': 'background-color: #CDCDCD;'}),
            "cumulativeRoundEight": forms.NumberInput(attrs={'readonly': 'readonly', 'style': 'background-color: #CDCDCD;'}),
            "subtotalRoundNine": forms.NumberInput(attrs={'readonly': 'readonly', 'style': 'background-color: #CDCDCD;'}),
            "cumulativeRoundNine": forms.NumberInput(attrs={'readonly': 'readonly', 'style': 'background-color: #CDCDCD;'}),
            "subtotalRoundTen": forms.NumberInput(attrs={'readonly': 'readonly', 'style': 'background-color: #CDCDCD;'}),
            "cumulativeRoundTen": forms.NumberInput(attrs={'readonly': 'readonly', 'style': 'background-color: #CDCDCD;'}),
            "score": forms.NumberInput(attrs={'readonly': 'readonly', 'style': 'background-color: #CDCDCD;'})

        }