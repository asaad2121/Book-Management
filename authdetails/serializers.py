from rest_framework import serializers
from .models import bookDet,authorDet

class AuthorDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = authorDet
        fields = ['id','auth_name']

class BookDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = bookDet
        exclude = ['book_author']

class BookAuthorDetailsSerializer(serializers.ModelSerializer):
    book_author = AuthorDetailsSerializer()
    class Meta:
        model = bookDet
        fields = '__all__'
        depth = 1