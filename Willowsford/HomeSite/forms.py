from django import forms

class emailForm(forms.Form):
    from_email = forms.EmailField(required=True)
    name = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)