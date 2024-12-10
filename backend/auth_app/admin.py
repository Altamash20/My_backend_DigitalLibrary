from django.contrib import admin
from auth_app.models import Book, Review 

# Register your models here.
admin.site.register(Book)
admin.site.register(Review)