from django.shortcuts import render
from app1.models import Beer1
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from app1.forms import SignUpForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

@login_required
def homepage_view(request):
    return render(request, 'html/base.html')

@login_required
def users_view(request):
    return render(request, 'html/beer_list.html')

class BeerList(ListView):
    model = Beer1
    template_name = 'html/beer_list.html'
    context_object_name = 'beer'

class BeerDetail(DetailView):
    model = Beer1
    template_name = 'html/beer_detail.html'
    context_object_name = 'beer'

class BeerCreate(CreateView):
    model = Beer1
    fields = '__all__'
    template_name = 'html/beer_form.html'

class BeerUpdate(UpdateView):
    model = Beer1
    fields = '__all__'
    template_name = 'html/beer_form.html'

class BeerDelete(DeleteView):
    model = Beer1
    template_name = 'html/beer_confirm_delete.html'
    success_url = reverse_lazy('differentname')

def logout_view(request):
    return render(request, 'html/logout.html')

def signup_view(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
        return HttpResponseRedirect('/accounts/login/')
    return render(request, 'html/signup.html', {'form': form})