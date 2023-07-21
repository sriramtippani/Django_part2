from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def f1(request):
    s = '<h1>f1 printed</h1>'
    return HttpResponse(s)

def f2(request):
    s = '<h1>f2 printed</h1>'
    return HttpResponse(s)

def f3(request):
    s = '<h1>f3 printed</h1>'
    return HttpResponse(s)

def f4(request):
    s = '<h1>f4 printed</h1>'
    return HttpResponse(s)

def f5(request):
    s = '<h1>f5 printed</h1>'
    return HttpResponse(s)