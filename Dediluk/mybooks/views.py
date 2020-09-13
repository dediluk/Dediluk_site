from django.shortcuts import render
from django.views.generic import ListView, DetailView
import request
from .models import Book


class BookList(ListView):
    model = Book
    template_name = 'mybooks/index.html'


def index(request):
    get_book = Book.objects.all()
    return render(request, 'mybooks/index.html', {'book': get_book, 'django': 'active'})


class BookDetail(DetailView):
    model = Book
    template_name = 'mybooks/book_detail.html'
