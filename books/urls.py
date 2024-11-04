from django.urls import path

from books.views import BooksView, BookView, BooksAPI

urlpatterns = [
    path('', BooksView.as_view(), name='list_book'),
    path('api/', BooksAPI.as_view(), name='list_book_api'),
    path('<int:pk>/', BookView.as_view(), name='detail_book'),
]
