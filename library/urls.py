from django.urls import path
from .views import BookList, BuyBook, PurchaseList

urlpatterns = [
    path('book-list', BookList.as_view()),
    path('purchase', BuyBook.as_view()),
    path('purchase-list', PurchaseList)
]
