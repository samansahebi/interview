from rest_framework.views import APIView
from .models import Book, Purchase
from .serializers import BookSerializer, PurchaseSerializer
from rest_framework.response import Response
from rest_framework import status


class BookList(APIView):
    def get(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BuyBook(APIView):
    def post(self, request):
        data = request.data
        serializer = PurchaseSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PurchaseList(APIView):
    def get(self, request):
        queryset = Purchase.objects.all()
        serializer = PurchaseSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

