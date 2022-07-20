from pyexpat import model
from django.db import models
from django.core import validators
# Create your models here.

class Book(models.Model):
    book_id = models.IntegerField(blank=True)
    isbn = models.CharField(max_length=100, unique=True, blank=True)
    author = models.CharField(max_length=200,null=True)
    title = models.CharField(max_length=50,null=True)
    year = models.CharField(max_length=1000, null=True)
    def __str__(self):
        return f"{self.title}"