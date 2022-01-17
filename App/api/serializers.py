from rest_framework import serializers
from App.models import Book


class BookListSerializer(serializers.ModelSerializer):
    #user = serializers.SlugRelatedField(slug_field='user', read_only=True)

    class Meta:
        model = Book
        fields = '__all__'