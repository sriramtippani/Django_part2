from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app1.forms import SignUpForm
from django.http import HttpResponseRedirect

# Create your views here.
def home_view(request):
    return render(request, 'html/home.html')

@login_required
def java_view(request):
    return render(request, 'html/javaexam.html')

@login_required
def python_view(request):
    return render(request, 'html/python.html')

@login_required
def aptitude_view(request):
    return render(request, 'html/aptitude.html')

def logout_view(request):
    return render(request, 'html/logout.html')

def signup_view(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request, 'html/signup.html', {'form': form})