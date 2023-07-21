from django.contrib import admin
from app_1.models import Java, Python

# Register your models here.
class JavaAdmin(admin.ModelAdmin):
    list_display = ['no', 'name', 'book', 'rate', 'year', 'language']

admin.site.register(Java, JavaAdmin)

class PythonAdmin(admin.ModelAdmin):
    list_display = ['no', 'name', 'book', 'rate', 'year', 'language']

admin.site.register(Python, PythonAdmin)

