from django.urls import path

from books.views import BooksView, BookFormView

urlpatterns = [
    path('books/', BooksView.as_view(), name='index'),
    path('books/new', BookFormView.as_view(), name='store'),
]
