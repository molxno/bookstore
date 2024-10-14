from django.forms import ModelForm, ModelMultipleChoiceField, ModelChoiceField

from books.models import Book, Author, Publisher


class BookForm(ModelForm):
    authors = ModelMultipleChoiceField(queryset=Author.objects.all(), label="Autores")
    publisher = ModelChoiceField(queryset=Publisher.objects.all(), label="Editora")

    class Meta:
        model = Book
        fields = ['title', 'authors', 'publisher', 'publication_date', 'isbn', 'pages', 'cover', 'stock', 'price']
        labels = {
            'title': 'Título',
            'authors': 'Autores',
            'publisher': 'Editora',
            'publication_date': 'Fecha de publicación',
            'isbn': 'ISBN',
            'pages': 'Páginas',
            'cover': 'Portada',
            'stock': 'Stock',
            'price': 'Precio',
        }

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['authors'].queryset = Author.objects.all()
        self.fields['publisher'].queryset = Publisher.objects.all()
        self.fields['authors'].label_from_instance = lambda obj: obj.name
        self.fields['publisher'].label_from_instance = lambda obj: obj.name
        self.fields['publication_date'].widget.attrs.update({'class': 'datepicker'})
        self.fields['cover'].widget.attrs.update({'class': 'file-field'})
        self.fields['price'].widget.attrs.update({'class': 'currency-field'})

    def save(self, commit=True):
        book = super().save(commit=False)
        if commit:
            book.save()
        book.authors.set(self.cleaned_data['authors'])
        return book
