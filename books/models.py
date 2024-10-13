from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name="Título")
    authors = models.ManyToManyField('Author', related_name='books', verbose_name="Autores")
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE, related_name='books', verbose_name="Editora")
    publication_date = models.DateField(verbose_name="Fecha de publicación")
    isbn = models.CharField(max_length=13, verbose_name="ISBN")
    pages = models.IntegerField(verbose_name="Páginas")
    cover = models.ImageField(upload_to='images', null=True, verbose_name="Portada")
    stock = models.IntegerField(default=0, verbose_name="Stock")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")

    def __str__(self):
        authors = ', '.join(self.authors.values_list('name', flat=True))
        cover = self.cover.url if self.cover else 'Sin portada'
        return f"{self.title} ({authors}) - {self.publisher.name} - {self.publication_date} - {self.isbn} - {self.pages} páginas - {cover} - {self.stock} unidades - ${self.price}"


class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    country = models.CharField(max_length=50, verbose_name="País")
    birth_date = models.DateField(verbose_name="Fecha de nacimiento")
    death_date = models.DateField(blank=True, null=True, verbose_name="Fecha de fallecimiento")
    biography = models.TextField(verbose_name="Biografía")

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    foundation_date = models.DateField(verbose_name="Fecha de fundación")
    address = models.TextField(verbose_name="Dirección")

    def __str__(self):
        return self.name
