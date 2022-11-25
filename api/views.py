from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import bookShortSerializer, bookDetailsSerializer

@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serializer = bookShortSerializer(books, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def book_details(request,pk):
    book = Book.objects.get(id=pk)
    serializer = bookDetailsSerializer(book)
    return Response(serializer.data)

@api_view(['POST'])
def add_book(request):
    serializer = bookDetailsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def update_book(request):
    book=Book.objects.get(id=int(request.data['id']))
    serializer = bookDetailsSerializer(book,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_book(request):
    Book.objects.get(id=int(request.data['id'])).delete()
    return Response(status=201)
