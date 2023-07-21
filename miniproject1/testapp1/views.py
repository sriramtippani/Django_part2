from django.shortcuts import render
from testapp1.models import Exam

# Create your views here.
def home_view(request):
    page = Exam.objects.all()
    my_dict = {'page': page}
    return render(request, 'html/home.html', context=my_dict)