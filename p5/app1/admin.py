from django.contrib import admin
from app1.models import Hjob, Bjob, Pjob

class f1(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'phonenumber']
admin.site.register(Hjob, f1)

class f2(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'phonenumber']
admin.site.register(Bjob, f2)

class f3(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'phonenumber']
admin.site.register(Pjob, f3)