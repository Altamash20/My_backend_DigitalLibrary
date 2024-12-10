from django.db import models
from django.contrib.auth.models import User


# Books
# User
# Reviews

class Books(models.Model):
    class TypeChoices(models.TextChoices):
        LITERARY = 'LR', 'Literary'
        HISTORY = 'HS', 'History'
        HORROR = 'HR', 'Horror'
        FICTION = 'FN', 'Fiction'
        SCIENCE = 'SCN', 'Science'
        OTHER = 'OTH', 'Other' 
    Title = models.CharField(max_length=100)
    Author = models.CharField(max_length=100)
    ISBN = models.IntegerField()
    Genre = models.CharField(max_length=100, choices=TypeChoices.choices)
    Cover_Image_URL = models.URLField(default='')

    def __str__(self):
        return self.title 
    

class Review(models.Model):
    Username = models.ForeignKey(User, on_delete=models.CASCADE)
    Title = models.ForeignKey(Books, on_delete=models.CASCADE)
    Rating = models.PositiveSmallIntegerField()
    Comment = models.CharField(max_length=200)

def __str__(self):
    return f"Rating: {self.rating}"
    
