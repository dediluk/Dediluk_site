from django.conf import settings
from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls.static import static

app_name = 'mybooks'

urlpatterns = [
                  path('', index),
                  path('/<int:pk>/', BookDetail.as_view(), name='detail')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
