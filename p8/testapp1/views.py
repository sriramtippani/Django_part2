from django.shortcuts import render
from testapp1.models import FilterModel

# Create your views here.
def test_view(request):
    form = FilterModel.objects.all()
    my_dict = {'form': form}
    return render(request, 'html/test.html', context=my_dict)