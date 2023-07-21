from django import forms
from django.core import validators
import captcha.fields


class CaptchaField:
    pass


class FeedBackForm(forms.Form):
    name = forms.CharField()
    rollno = forms.IntegerField()
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea)
    password = forms.CharField(label='Enter Password', widget=forms.PasswordInput)
    rpassword = forms.CharField(label='Re-enter Password', widget=forms.PasswordInput)
    captcha = CaptchaField()




    def clean(self):
        alldata = super().clean()
        inputname = alldata['name']
        if inputname[0].lower() != 'd':
            raise forms.ValidationError('Name parameter should starts with d')
        if len(inputname) < 5:
            raise forms.ValidationError('The minimum number of character of the name should be 5')

        inputrollno = alldata['rollno']
        if inputrollno <= 100:
            raise forms.ValidationError('The rollno is equal and greater than 100')

        inputemail = alldata['email']
        if inputemail[-10:] != '@gmail.com':
            raise forms.ValidationError('Email Extension should be gmail.')

        inputfeedback = alldata['feedback']
        if len(inputfeedback) < 20 and len(inputfeedback) > 10:
            raise forms.ValidationError('The maximum letters is 20 and minimum letters are 10')

        pwd = alldata['password']
        rpwd = alldata['rpassword']
        if pwd != rpwd:
            raise forms.ValidationError('Both passwords must be same')
