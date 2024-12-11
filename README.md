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
you can get other information like First name, Email, Username etc for required user by replacing 'password' in above command 
<br>
<br>
<br>
to retrieve all books-
<br>
Book.objects.all()
<br>
To get detail about different attribute of required books, you can use same command as in case of users
<br>
To see how to write tests for APIs here please see tests.py file and viga_script.py file in script directory
<br>
Command to check whether tests running successfully-
<br>
python manage.py test
<br>
Command to run scripts -
<br>
python manage.py runscript <script file name>
<br>
Note: Do not use .py extension with file in above runscript command
<br>
<br>
<br>
Note: Always check whether the backend server is running before using Endpoints URL
<br>
Command to run backend server: python manage.py runserver

