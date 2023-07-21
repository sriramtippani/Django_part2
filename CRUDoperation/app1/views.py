from django.db.models import Q
from django.shortcuts import render, redirect
from app1.models import Employee
from app1.forms import EmployeeForm

# Create your views here.
def index_view(request):
    # emp_list = Employee.objects.all()
    # emp_list = Employee.objects.filter(ename__startswith='s', esal__lt=27000)
    # emp_list = Employee.objects.filter(ename__startswith='v') | Employee.objects.filter(esal__lt=27000)
    emp_list = Employee.objects.filter(~Q(ename__startswith='v'))
    return render(request, 'html/index.html', {'emp_list': emp_list})

def insert_view(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return index_view(request)
    return render(request, 'html/insert.html', {'form': form})

def delete_view(request, id):
    delete1 = Employee.objects.get(id=id)
    delete1.delete()
    return index_view(request)

def update_view(request, id):
    update1 = Employee.objects.get(id=id)
    form = EmployeeForm(instance=update1)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=update1)
        if form.is_valid():
            form.save()
        return index_view(request)
    return render(request, 'html/update.html', {'form': form})