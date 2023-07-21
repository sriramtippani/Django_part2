from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app_1.models import Java, Python
from app_1.forms import JavaForm, PythonForm, SignUpForm

# Create your views here.
def homepage_view(request):
    return render(request, 'html/home.html')

@login_required
def imagepage_view(request):
    type = 'photo'
    return render(request, 'html/image.html', {'type': type})

@login_required
def insertJava_view(request):
    java_list = Java.objects.all()
    form = JavaForm()
    if request.method == 'POST':
        form = JavaForm(request.POST)
        if form.is_valid():
            form.save()
        return homepage_view(request)
    return render(request, 'html/form.html', {'form': form, 'java_list': java_list})

@login_required
def updatejava_view(request, id):
    update1 = Java.objects.get(id=id)
    form = JavaForm(instance=update1)
    if request.method == 'POST':
        form = JavaForm(request.POST, instance=update1)
        if form.is_valid():
            form.save()
        return insertJava_view(request)
    return render(request, 'html/update.html', {'form': form})

@login_required
def delete_view(request, id):
    delete1 = Java.objects.get(id=id)
    delete1.delete()
    return insertJava_view(request)

@login_required
def insertpython_view(request):
    python_list = Python.objects.all()
    form = PythonForm()
    if request.method == 'POST':
        form = PythonForm(request.POST)
        if form.is_valid():
            form.save()
        return homepage_view(request)
    return render(request, 'html/form2.html', {'form': form, 'python_list': python_list})

@login_required
def updatepython_view(request, id):
    update2 = Python.objects.get(id=id)
    form = PythonForm(instance=update2)
    if request.method == 'POST':
        form = PythonForm(request.POST, instance=update2)
        if form.is_valid():
            form.save()
        return insertpython_view(request)
    return render(request, 'html/update2.html', {'form': form})

@login_required
def deletepython_view(request, id):
    delete2 = Python.objects.get(id=id)
    delete2.delete()
    return insertpython_view(request)

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

def logout_view(request):
    return render(request, 'html/logout.html')
