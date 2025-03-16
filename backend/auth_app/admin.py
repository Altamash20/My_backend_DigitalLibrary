from django.contrib import admin
from auth_app.models import Book, Review

# Register your models here.
admin.site.register(Book)
admin.site.register(Review)
# admin.site.register(User) , model user is already registered, no need to register again here else gives error