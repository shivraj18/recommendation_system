from django.urls import path
from . import views
from .views import UploadFileView
urlpatterns = [
    path("",views.index),
    path("suggested-book", views.suggested_book, name="book-title")
]