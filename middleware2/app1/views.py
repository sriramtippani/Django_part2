from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage_view(request):
    print('View page')
    return HttpResponse('<h1>Hi this is home page view.</h1>')
