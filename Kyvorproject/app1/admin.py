from django.contrib import admin
from app1.models import Detail1Model

# Register your models here.

class Detail1Admin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'preffered_name', 'title_name', 'email', 'contact_no', 'contact_ext', 'join_date', 'join_date_format', 'team', 'job_title']


admin.site.register(Detail1Model, Detail1Admin)