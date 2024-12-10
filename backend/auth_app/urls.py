from django.urls import path
from . import views


urlpatterns = [
    path('books_management/',views.books_page, name='books_management'),
    path('register/',views.register_page, name='register'),
    path('login/',views.login_page, name='login')

]