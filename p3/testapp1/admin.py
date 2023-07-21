from django.contrib import admin
from testapp1.models import Employee

# Register your models here.
class e1(admin.ModelAdmin):
    list_display = ['ename', 'esal', 'eaddr']

admin.site.register(Employee, e1)
