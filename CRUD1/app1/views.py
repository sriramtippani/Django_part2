from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from app1.models import *
from django.urls import reverse_lazy

# Create your views here.
class BookView(ListView):
    model = Book
    template_name = 'html/books.html'
    context_object_name = 'books'


class BookDetail(DetailView):
    model = Book
    template_name = 'html/book_detail.html'
    context_object_name = 'books'


class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    template_name = 'html/book_form.html'

class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'
    template_name = 'html/book_form.html'
    context_object_name = 'books'

class BookDelete(DeleteView):
    model = Book
    template_name = 'html/book_confirm_delete.html'
    success_url = reverse_lazy('bookdelete')
