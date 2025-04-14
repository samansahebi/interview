from rest_framework.serializers import ModelSerializer

from library.models import Book, Purchase


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class PurchaseSerializer(ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'
