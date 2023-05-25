from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html', {'title': 'Главная страница'})

def afterindex(request):
    return render(request, 'main/login.html')