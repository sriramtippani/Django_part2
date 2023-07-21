from django.contrib import admin
from app1.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno', 'ename', 'esal', 'eaddr']

admin.site.register(Employee, EmployeeAdmin)