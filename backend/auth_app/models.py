from django.db import models
from django.contrib.auth.models import User
from .models import *


# Books
# User
# Reviews

class Book(models.Model):
    class TypeChoices(models.TextChoices):
        LITERARY = 'LR', 'Literary'
        HISTORY = 'HS', 'History'
        HORROR = 'HR', 'Horror'
        FICTION = 'FN', 'Fiction'
        SCIENCE = 'SCN', 'Science'
        OTHER = 'OTH', 'Other'
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True) 
    Title = models.CharField(max_length=100)
    Author = models.CharField(max_length=100)
    ISBN = models.IntegerField()
    Genre = models.CharField(max_length=100, choices=TypeChoices.choices)
    Cover_Image_URL = models.URLField(default='')

    def __str__(self):
        return self.Title 
    

class Review(models.Model):
    Username = models.ForeignKey(User, on_delete=models.CASCADE)
    Title = models.ForeignKey(Book, on_delete=models.CASCADE)
    Rating = models.PositiveSmallIntegerField()
    Comment = models.CharField(max_length=200)

    def __str__(self):
        return f"Rating: {self.rating}"
