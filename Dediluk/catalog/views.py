from django.shortcuts import render


def mainPage(request):
    return render(request, 'Dediluk/main_page.html')


def aboutMe(request):
    return render(request, 'Dediluk/about.html')
