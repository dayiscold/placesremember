from django.urls import path
from . import views

urlpatterns = [
    path('', views.afterindex, name='memories_home'),
    path('create', views.create, name='create')
]