from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.

def register_page(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        
        user = User.objects.filter(username=username)

        if user.exists():
            return redirect('/register/')
        
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
            email = email
            # password = password # save password as it is
        )

        user.set_password(password)
        user.save()

        return redirect('/register')
    
    return render(request, 'register.html')


def login_page(request):
    return render(request, 'login.html')
  

