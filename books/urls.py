from django.urls import path

from books.views import BooksView

urlpatterns = [
    path('', BooksView.as_view(), name='list_book'),
]
