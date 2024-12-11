Instructions to Setup and use APIs: (Author- Mohammad Altamash)
<br>
1) Backend server is running at localhost:8000/
<br>
2) Our backend application is named as auth_app
<br>
3) Endpoint to register as a user: localhost:8000/auth/register/
<br>
4) Endpoint to login for registered users: localhost:8000/auth/login/
<br>
5) Endpoint to add a new Book with its details: localhost:8000/auth/books_management/
<br>
(but remember you cannot land to ADD BOOK page without getting registered, and then login
<br>
6) To retrieve the details of the registered users and saved books from database, we can use interactive Python shell in terminal window:
<br>
Command to access Python interactive shell:
<br>
python manage.py shell
<br>
Now follow below commands:
<br>
from django.contrib.auth.models import *
<br>
<br>
to retrieve all users-
User.objects.all()
<br>
to get password of user(encrypted with Hashing algorithm)-
<br>
User.objects.all()[index of required user].password
<br>
<br>
<br>
to retrieve all books-
<br> 
