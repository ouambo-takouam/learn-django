from django import forms

class LeadForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=20)
    last_name = forms.CharField(label="Last Name", max_length=20)
    age = forms.IntegerField(min_value=0)
