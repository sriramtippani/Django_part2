from django.shortcuts import render
from app1.models import Hjob, Bjob, Pjob

# Create your views here.
def hm(request):
    return render(request, 'html/index.html')

def hy(request):
    jobs_list = Hjob.objects.all()
    my_dict = {'jobs_list': jobs_list}
    return render(request, 'html/h1.html', context=my_dict)


def ba(request):
    jobs_list = Bjob.objects.all()
    my_dict = {'jobs_list': jobs_list}
    return render(request, 'html/b1.html', context=my_dict)


def pu(request):
    jobs_list = Pjob.objects.all()
    my_dict = {'jobs_list': jobs_list}
    return render(request, 'html/p1.html', context=my_dict)
