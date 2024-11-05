from django.contrib.auth.models import User
from django.db import models

from books.models import Book


# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)

    def calculate_total(self):
        return sum(item.book.price * item.quantity for item in self.orderbook_set.all())

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"


class OrderBook(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Order {self.order.id} - {self.book.title}"
