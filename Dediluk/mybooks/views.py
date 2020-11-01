from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.urls import reverse
from .forms import CreateBookForm, CreateAuthorForm
from .models import Book, Author
from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404


def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'mybooks/authors_list.html', {'authors': authors})


def index(request):
    print('В индексе')
    print('В индексе')
    get_book = Book.objects.all()
    paginator = Paginator(get_book, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'mybooks/index.html', {'page_obj': page_obj})


class BookDetail(DetailView):
    model = Book
    template_name = 'mybooks/book_detail.html'


def authorDetail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    context = Book.objects.filter(author_name=pk)
    return render(request, 'mybooks/author_detail.html', {'author': author, 'books': context})


class SearchResult(ListView):
    model = Book
    template_name = 'dediluk/search.html'

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Book.objects.filter(Q(title__icontains=query.lower()) | Q(title__icontains=query.title()))
        return object_list


def addBookPage(request):
    form = CreateBookForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("mybooks:index"))
    return render(request, 'mybooks/add_book.html', {'form': form})


def addAuthorPage(request):
    form = CreateAuthorForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("mybooks:authors_list"))
    return render(request, 'mybooks/add_author.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    get_book = Book.objects.all()
    return HttpResponseRedirect(reverse("mybooks:index"))


@user_passes_test(lambda u: u.is_superuser)
def delete_author(request, pk):
    author = get_object_or_404(Author, pk=pk)
    author.delete()
    get_author = Author.objects.all()
    return HttpResponseRedirect(reverse("mybooks:index"))
