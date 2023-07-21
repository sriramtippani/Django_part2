from django import forms
from app_1.models import Java, Python
from captcha.fields import CaptchaField
from django.contrib.auth.models import User

class JavaForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Java
        fields = '__all__'


class PythonForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Python
        fields = '__all__'

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
