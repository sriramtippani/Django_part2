from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(x):
    s = 'their final.'
    return HttpResponse(s)
