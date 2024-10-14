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


class BookFormView(FormView):
    template_name = 'books/add_book.html'
    form_class = BookForm
    success_url = reverse_lazy('list_book')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
