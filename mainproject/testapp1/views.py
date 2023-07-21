from django.shortcuts import render
from testapp1.models import Movie
from testapp1.forms import MovieForm
from django import forms

# Create your views here.


def index_view(request):
    return render(request, 'html/index.html')

def addmovie_view(request):
    form = MovieForm()
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid:
            form.save()
        return index_view(request)
    my_dict = {'form': form}
    return render(request, 'html/addmovie.html', context=my_dict)

def listmovie_view(request):
    movie_list = Movie.objects.all()
    my_dict = {'movie_list': movie_list}
    return render(request, 'html/listmovie.html', context=my_dict)