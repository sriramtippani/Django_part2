from django.shortcuts import render
from testapp1.forms import AddSessionForm

# Create your views here.
def additem_view(request):
    form = AddSessionForm()
    if request.method == 'POST':
        name = request.POST['name']
        quantity = request.POST['quantity']
        request.session[name] = quantity
    return render(request, 'html/additem.html', {'form': form})


def display_view(request):
    return render(request, 'html/display.html')