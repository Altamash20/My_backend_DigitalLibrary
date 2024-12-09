from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout

# Create your views here.

def register_page(request):
    return render(request, 'register.html')


def login_page(request):
    return render(request, 'login.html')
  

