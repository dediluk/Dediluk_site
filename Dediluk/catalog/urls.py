from django.conf import settings
from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls.static import static

app_name = 'catalog'

urlpatterns = [
                  path('', mainPage, name='main_page'),
                  path('about', aboutMe, name='about')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
