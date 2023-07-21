from django.contrib import admin
from testapp1.models import Exam

# Register your models here.
class ExamAdmin(admin.ModelAdmin):
    list_display = ['question', 'option1', 'option2', 'option3', 'option4', 'correct']

admin.site.register(Exam, ExamAdmin)