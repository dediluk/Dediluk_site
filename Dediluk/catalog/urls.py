from django.conf import settings
from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls.static import static

app_name = 'catalog'

urlpatterns = [
                  path('', mainPage, name='main_page'),
                  path('about', aboutMe, name='about'),
                  path('user_detail/<str:username>', user_profile, name='about_user'),
                  path('change_password/<str:username>', change_password, name='change_password'),
                  path('accounts/register/', RegisterFormView.as_view(), name='register')
                  # path('user_detail/<int:pk>', UserDetail.as_view(), name='about_user')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
