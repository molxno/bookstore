from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, ListView
from rest_framework.response import Response
from rest_framework.views import APIView

from books.forms import BookForm
from books.models import Book
from books.serializers import BookSerializer


# Create your views here.
class BooksView(ListView):
    template_name = 'books/list_book.html'
    model = Book
    context_object_name = 'books'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total'] = self.get_queryset().count()
        return context


class BookView(TemplateView):
    template_name = 'books/detail_book.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = Book.objects.get(pk=kwargs['pk'])
        return context


class BooksAPI(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
