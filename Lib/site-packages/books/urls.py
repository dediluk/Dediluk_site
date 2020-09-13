from django.conf.urls import url

from books.views import BooksList
from books.views import BookDetail

urlpatterns = [
    url(r'^$', BooksList.as_view(), name='books-index'),
    url(r'^(?P<slug>[-\w]+)$', BookDetail.as_view(), name='books-details'),
]
