from .models import Book
from rest_framework import serializers

class bookDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','ISBN','title','author','published','publisher','price','available']

class bookShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title','available']