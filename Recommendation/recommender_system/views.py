from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from recommender_system.models import Book
from .recommender import recommendation_system
import io, csv, pandas as pd
from rest_framework.response import Response
from .serializers import FileUploadSerializer, SaveFileSerializer

# Create your views here.

def index(request):
    book = Book.objects.all()
    return render(request, "recommender_system/index.html",{
        "books": book
    })


def suggested_book(request):
    book_id = request.GET.get('book_id')
    recommended_book = recommendation_system(int(book_id))
    return render(request, "recommender_system/suggested_book.html", {
        "books": recommended_book,
        "bookID": book_id
    })

class UploadFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            new_file = Book(
                       title = row["title"],
                       author= row["authors"],
                       year= row["original_publication_year"],
                       book_id = row["book_id"],
                       isbn = row["isbn"]
                       )
            new_file.save()
        return Response({"status": "success"},
)