from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')

def afterindex(request):
    return render(request, 'main/login.html')