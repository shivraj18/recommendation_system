from rest_framework import serializers
from .models import Book
class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()
class SaveFileSerializer(serializers.Serializer):
    
    class Meta:
        model = Book
        fields = "__all__"