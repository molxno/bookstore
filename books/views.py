from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from books.forms import BookForm
from books.models import Book


# Create your views here.
class BooksView(TemplateView):
    template_name = 'books/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        return context


class BookFormView(FormView):
    template_name = 'books/store.html'
    form_class = BookForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
