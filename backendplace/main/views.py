from django.shortcuts import render, redirect
from .models import Tablish
from .forms import TablishForm

def index(request):
    return render(request, 'main/index.html', {'title': 'Главная страница'})

def afterindex(request):
    memory = Tablish.objects.order_by('-date')
    return render(request, 'main/login.html', {'memory': memory})

def create(request):
    error = ''
    if request.method == 'POST':
        form = TablishForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('memories_home')
        else:
            error = 'Неверное заполнение формы'

    form = TablishForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', data)