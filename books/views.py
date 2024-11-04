from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, ListView
from books.forms import BookForm
from books.models import Book


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
