from rest_framework.decorators import api_view
from rest_framework.response import Response
from books.models import Book
from .serializers import BookSerializer
from rest_framework import status


@api_view(["GET"])
def getRoutes(request):
    routes = [
        "POST /books/",
        "GET /books/",
        "GET /books/:id/",
        "PUT books/:id/",
        "DELETE /books/:id",
    ]
    return Response(routes)


@api_view(["GET"])
def getBooks(request):

    book = Book.objects.all()
    serializer = BookSerializer(book, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getBook(request, pk):
    try:
        book = Book.objects.get(isbn=pk)
    except Book.DoesNotExist:
        return Response({"detail": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = BookSerializer(book, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def createBook(request):
    serializer = BookSerializer(data=request.data)
    if (serializer.is_valid()):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def deleteBook(request, pk):
    try:
        book = Book.objects.get(isbn=pk)
        book.delete()
        return Response({"message": "Book deleted successfully"}, status=status.HTTP_200_OK)
    except Book.DoesNotExist:
        return Response({"message": "Book not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(["PUT"])
def updateBook(request, pk):
    try:
        book = Book.objects.get(isbn=pk)
    except Book.DoesNotExist:
        return Response({"message": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = BookSerializer(book, request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
