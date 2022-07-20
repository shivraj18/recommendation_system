from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author","year", "book_id","isbn"]
admin.site.register(Book)


# Register your models here.
