from django.contrib import admin
from testapp1.models import Detailsinfo

# Register your models here.
class E1(admin.ModelAdmin):
    list_display = ['eno', 'ename', 'esal', 'eaddr']

admin.site.register(Detailsinfo, E1)