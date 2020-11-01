from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, FormView
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import ugettext as _
from django.contrib.auth.forms import UserCreationForm


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/accounts/login/?next=/mybooks"
    template_name = 'registration/register.html'

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        print('=====================================')
        return super(RegisterFormView, self).form_invalid(form)


# @login_required
def mainPage(request):
    print(request.user.get_username())
    return render(request, 'Dediluk/main_page.html')


def aboutMe(request):
    return render(request, 'Dediluk/about.html')


def user_profile(request, username):
    user = User.objects.get(Q(username=username.title()) | Q(username=username.lower()))
    return render(request, 'Dediluk/user_detail.html', {'userdetail': user})


def change_password(request, username):
    print(request.method == 'POST')
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, _('Ваш пароль был успешно изменен!'))
            return redirect('catalog:main_page')
        else:
            messages.error(request, _("Данные введены некорректно"))
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'Dediluk/change_password.html', {'form': form})
    # if username.lower() == request.user.get_username().lower():
    #     return render(request, 'Dediluk/change_password.html')
    # u = User.objects.get(username=username)


class UserDetail(DetailView):
    model = User
    template_name = 'Dediluk/user_detail.html'
