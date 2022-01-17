from rest_framework.response import Response
from rest_framework.views import APIView

from App.models import Book
from .serializers import BookListSerializer

class BookListView(APIView):
    def get(self, request):
        books = Book.objects
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)