from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'html/home.html')


def age_view(request):
    print(request.COOKIES)
    name = request.GET['name']
    my_dict = {'name': name}
    response = render(request, 'html/age.html', context=my_dict)
    response.set_cookie('name', name)
    return response

def gf_view(request):
    name = request.COOKIES['name']
    age = request.GET['age']
    my_dict = {'name': name}
    response = render(request, 'html/gf.html', context=my_dict)
    response.set_cookie('age', age)
    return response

def end_view(request):
    name = request.COOKIES['name']
    age = request.COOKIES['age']
    gf = request.GET['gf']
    my_dict = {'name': name, 'age': age, 'gf': gf}
    response = render(request, 'html/end.html', context=my_dict)
    response.set_cookie('gf', gf)
    return response
