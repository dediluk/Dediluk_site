from django.views.generic import ListView
from django.views.generic import DetailView

from books.models import Book


class BooksList(ListView):
    def get_queryset(self):
        return Book.on_site.published()


class BookDetail(DetailView):
    def get_queryset(self):
        return Book.on_site.published()
