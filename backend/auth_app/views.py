from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.contrib import messages
from .models import *



# Create your views here.


def books_page(request):
    
    if request.method == "POST":
        data = request.POST
        Title = data.get('Title')
        Author = data.get('Author')
        ISBN = data.get('ISBN')
        Genre = data.get('Genre')
        Cover_Image_URL = data.get('Cover_Image_URL')
        
        book = Book.objects.filter(ISBN=ISBN)
        
        if book.exists():
            messages.info(request, 'ISBN already taken!')
            return redirect('/auth/books_management/')
        
        book = Book.objects.create(
            Title = Title,
            Author = Author,
            ISBN = ISBN,
            Genre = Genre,
            Cover_Image_URL = Cover_Image_URL,
        )

        messages.info(request, 'Book info submitted successfully!')

        
        return redirect('/books_management/')
    
    return render(request, 'books.html')




def register_page(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, 'Username already taken!')
            return redirect('/auth/register/')
        
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
            email = email
            # password = password # save password as it is
        )

        user.set_password(password)
        user.save()

        messages.info(request, 'Account created successfully!')

        return redirect('/register')
    
    return render(request, 'register.html')




def login_page(request):
    return render(request, 'login.html')
  

