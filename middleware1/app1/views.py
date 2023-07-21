from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage_view(request):
    print(10/0)
    return HttpResponse('<h1>Hello This is from home page view.</h1>')
