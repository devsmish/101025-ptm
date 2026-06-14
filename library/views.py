from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from library.serializers.books import BookListSerializer
from library.models import Book




@api_view(['GET',])
def book_list_view(request):
    # 1. Получить набор данных
    books = Book.objects.all()

    # 2. Данные -- сложные объекты, нужно упростить
    # первый параметр -- это instance, то есть то, что мы хотим преобразить.
    # по умолчанию ВСЕ сериазизаторы работают с настройкой только на один объект.
    # если мы передаём много объектов (список), то сериализатору нужно помочь, добавив параметр
    # many=True. Так сериализатор поймёт, что пришшло много объектов и не будет пытаться
    # получить у списка через точку, допустим, name книги. Ведь теперь он знает, что перед ним не
    # один объект, а N объектов в списке.
    serializer = BookListSerializer(books, many=True)

    # 3. Вернуть ответет
    return Response(
        data=serializer.data,
        status=200 # пока что статусы возвращаем явно в виде циферок. Потом сделаем красивее
        # и будем использовать специальные константы
    )


@api_view(['GET', 'POST'])
def book_list_create(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookListSerializer(books, many=True)
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )
    if request.method == 'POST':
        serializer = BookListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET', 'PUT', 'DELETE'])
def book_read_update_delete(request, pk):
    # try:
    #     book = Book.objects.get(pk=pk)
    # except Book.DoesNotExist:
    #     return Response(
    #         status=status.HTTP_404_NOT_FOUND
    #     )

    book = get_object_or_404(Book, pk=pk)

    if request.method == 'GET':
        serializer = BookListSerializer(book)
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )
    if request.method == 'PUT':
        serializer = BookListSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    if request.method == 'DELETE':
        book.delete()
        return Response(
            {'message': 'Book deleted', },
            status=status.HTTP_204_NO_CONTENT
        )


class BookListCreateAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookListSerializer(books, many=True)

        return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
    def post(self, request):
        serializer = BookListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class BookDetailAPIView(APIView):
    def get(self, request, pk):
        pass

    def put(self, request, pk):
        pass

    def delete(self, request, pk):
        pass
