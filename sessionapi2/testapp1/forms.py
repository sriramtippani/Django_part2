from django import forms

class AddSessionForm(forms.Form):
    name = forms.CharField()
    quantity = forms.IntegerField()
