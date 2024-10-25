import requests
from django.core.files import File
from django.core.management.base import BaseCommand
from books.models import Book, Author, Publisher
from io import BytesIO


# Función para descargar imagen y devolver un archivo temporal
def download_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BytesIO(response.content)
    else:
        print(f"Error al descargar la imagen de {url}")
        return None


class Command(BaseCommand):
    help = 'Seed database with books, authors, and publishers'

    def handle(self, *args, **kwargs):
        # Crear Autores
        author1 = Author.objects.create(
            name='Gabriel García Márquez',
            country='Colombia',
            birth_date='1927-03-06',
            death_date='2014-04-17',
            biography="Un escritor colombiano, conocido por su novela 'Cien años de soledad'."
        )

        author2 = Author.objects.create(
            name='J.K. Rowling',
            country='Reino Unido',
            birth_date='1965-07-31',
            death_date=None,
            biography="Autora británica conocida por la serie de Harry Potter."
        )

        author3 = Author.objects.create(
            name='Antoine de Saint-Exupéry',
            country='Francia',
            birth_date='1900-06-29',
            death_date='1944-07-31',
            biography="Un escritor, ilustrador y piloto francés, autor de 'El Principito'."
        )

        # Crear Editoriales
        publisher1 = Publisher.objects.create(
            name='Editorial Sudamericana',
            foundation_date='1948-01-01',
            address='Buenos Aires, Argentina'
        )

        publisher2 = Publisher.objects.create(
            name='Bloomsbury Publishing',
            foundation_date='1986-02-26',
            address='Londres, Reino Unido'
        )

        publisher3 = Publisher.objects.create(
            name='Reynal & Hitchcock',
            foundation_date='1933-01-01',
            address='Nueva York, Estados Unidos'
        )

        # URL de imágenes para los libros
        book_images = [
            'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcR-_qFlRxa5Ozof4LnQb6m3QZYNCh4JRxa2Xc0cCMwVn_3Sdyry',
            'https://books.google.com.co/books/content?id=2zgRDXFWkm8C&pg=PP1&img=1&zoom=3&hl=en&bul=1&sig=ACfU3U0QXCxkCmsHBYCkHRDQfplIdcWHhw&w=1280',
            'https://books.google.com.co/books/publisher/content?id=6-eREAAAQBAJ&pg=PA1&img=1&zoom=3&hl=en&bul=1&sig=ACfU3U2vxpyu5_RklS5ATrJ2XWXo6lsRdQ&w=1280'
        ]

        # Crear libros
        books_data = [
            {
                'title': 'Cien Años de Soledad',
                'description': 'La obra maestra de Gabriel García Márquez, un clásico de la literatura universal.',
                'authors': [author1],
                'publisher': publisher1,
                'publication_date': '1967-06-05',
                'isbn': '9780060883287',
                'pages': 417,
                'stock': 10,
                'price': 15.99,
                'cover_url': book_images[0]
            },
            {
                'title': 'Harry Potter y la Piedra Filosofal',
                'description': 'La primera novela de la serie de Harry Potter, escrita por J.K. Rowling.',
                'authors': [author2],
                'publisher': publisher2,
                'publication_date': '1997-06-26',
                'isbn': '9780747532699',
                'pages': 223,
                'stock': 5,
                'price': 20.99,
                'cover_url': book_images[1]
            },
            {
                'title': 'El Principito',
                'description': 'Un cuento poético y filosófico del escritor francés Antoine de Saint-Exupéry.',
                'authors': [author3],
                'publisher': publisher3,
                'publication_date': '1943-04-06',
                'isbn': '9780156012195',
                'pages': 96,
                'stock': 7,
                'price': 10.99,
                'cover_url': book_images[2]
            }
        ]

        for book_data in books_data:
            # Crear el libro
            book = Book.objects.create(
                title=book_data['title'],
                description=book_data['description'],
                publisher=book_data['publisher'],
                publication_date=book_data['publication_date'],
                isbn=book_data['isbn'],
                pages=book_data['pages'],
                stock=book_data['stock'],
                price=book_data['price'],
            )

            # Asignar autores
            book.authors.set(book_data['authors'])

            # Descargar imagen de la URL
            image_content = download_image(book_data['cover_url'])
            if image_content:
                # Guardar imagen en el campo 'cover'
                image_name = f"{book_data['title'].replace(' ', '_').lower()}.jpg"
                book.cover.save(image_name, File(image_content), save=True)

            print(f"Libro '{book.title}' creado con éxito.")
