from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from app1.forms import Detail1Form, SignUpForm
from app1.models import Detail1Model
from django.views.generic import DeleteView
from django.urls import reverse_lazy

# Create your views here.

def homepage_view(request):
    return render(request, 'html/home.html')

@login_required
def listpage_view(request):
    emp_list = Detail1Model.objects.all()
    return render(request, 'html/list.html', {'emp_list': emp_list})

@login_required
def insert_table_view(request):
    form = Detail1Form()
    if request.method == 'POST':
        form = Detail1Form(request.POST)
        if form.is_valid():
            form.save()
        return listpage_view(request)
    return render(request, 'html/form1.html', {'form': form})

@login_required
def detail_view(request, id):
    emp_list = Detail1Model.objects.get(id=id)
    return render(request, 'html/detail.html', {'emp_list': emp_list})

@login_required
def update_table_view(request, id):
    emp_list = Detail1Model.objects.get(id=id)
    form = Detail1Form(instance=emp_list)
    if request.method == 'POST':
        form = Detail1Form(request.POST, instance=emp_list)
        if form.is_valid():
            form.save()
        return listpage_view(request)
    return render(request, 'html/form2.html', {'form': form})

class delete_table_view(DeleteView):
    model = Detail1Model
    template_name = 'html/delete.html'
    success_url = reverse_lazy('listpage')

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