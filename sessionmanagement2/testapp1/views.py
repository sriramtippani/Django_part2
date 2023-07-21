from django.shortcuts import render
from testapp1.forms import AdditemForm

# Create your views here.
def home_view(request):
    return render(request, 'html/home.html')

def additem_view(request):
    form = AdditemForm()
    response = render(request, 'html/additem.html', {'form': form})
    if request.method == 'POST':
        form = AdditemForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['itemname']
            quantity = form.cleaned_data['quantity']
            response.set_cookie(name, quantity, 60)
    return response


def result_view(request):
    return render(request, 'html/result.html')