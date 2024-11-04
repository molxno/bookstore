from django.contrib import admin

from books.models import Book, Publisher, Author


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ['title', 'description', 'publisher', 'publication_date', 'isbn', 'pages', 'stock', 'price']
    search_fields = ['title', 'publisher__name', 'isbn']


admin.site.register(Book, BookAdmin)


class PublisherAdmin(admin.ModelAdmin):
    model = Publisher
    list_display = ['name', 'foundation_date', 'address']
    search_fields = ['name']


admin.site.register(Publisher, PublisherAdmin)


class AuthorAdmin(admin.ModelAdmin):
    model = Author
    list_display = ['name', 'country', 'birth_date', 'death_date']
    search_fields = ['name']


admin.site.register(Author, AuthorAdmin)
