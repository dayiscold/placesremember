from django.shortcuts import render
from .models import Tablish

def index(request):
    return render(request, 'main/index.html', {'title': 'Главная страница'})

def afterindex(request):
    memory = Tablish.objects.order_by('date')
    return render(request, 'main/login.html', {'memory': memory})
