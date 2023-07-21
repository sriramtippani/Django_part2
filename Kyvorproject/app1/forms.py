from django import forms
from app1.models import Detail1Model
from django.contrib.auth.models import User


class Detail1Form(forms.ModelForm):
    class Meta:
        model = Detail1Model
        fields = '__all__'

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
