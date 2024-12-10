from django.contrib import admin
from auth_app.models import Books, Review 

# Register your models here.
admin.site.register(Books)
admin.site.register(Review)