from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def t1(request):
    s = '<h1>got it AppOne</h1>'
    return HttpResponse(s)