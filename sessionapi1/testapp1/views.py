from django.shortcuts import render
from testapp1.forms import *

# Create your views here.
def name_view(request):
    form = NameForm()
    return render(request, 'html/home.html', {'form': form})

def age_view(request):
    name = request.GET['name']
    request.session['name'] = name
    form = AgeForm()
    return render(request, 'html/age.html', {'form': form, 'name': name})

def gf_view(request):
    age = request.GET['age']
    request.session['age'] = age
    name = request.session['name']
    form = GfForm()
    return render(request, 'html/gf.html', {'form': form, 'name': name, 'age': age})

def results_view(request):
    gf = request.GET['gf']
    request.session['gf'] = gf
    return render(request, 'html/results.html')