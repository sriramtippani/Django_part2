from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def t2(request):
    s1 = '<h1>got it AppTwo</h1>'
    return HttpResponse(s1)