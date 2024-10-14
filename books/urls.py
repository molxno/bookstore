from django.urls import path

from books.views import BooksView, BookFormView

urlpatterns = [
    path('', BooksView.as_view(), name='list_book'),
    path('add', BookFormView.as_view(), name='add_book'),
]
