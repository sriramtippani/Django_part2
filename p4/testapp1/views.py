from django.shortcuts import render
from testapp1.models import Detailsinfo

# Create your views here.
def f11(request):
    emp_list = Detailsinfo.objects.all()
    my_dict = {'emp_list': emp_list}
    return render(request, 'htmlthings/index.html', context=my_dict)