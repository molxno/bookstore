from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView

from orders.forms import OrderBookForm
from orders.models import Order, OrderBook


# Create your views here.
class MyOrderView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'orders/my_order.html'
    context_object_name = 'order'

    def get_object(self, queryset=None):
        return Order.objects.filter(status=True, user=self.request.user).first()


class CreateOrderBookView(LoginRequiredMixin, CreateView):
    template_name = 'orders/create_order_book.html'
    form_class = OrderBookForm
    success_url = reverse_lazy('my_order')

    def form_valid(self, form):
        order, _ = Order.objects.get_or_create(user=self.request.user, status=True)
        form.instance.order = order
        form.instance.quantity = 1
        form.save()
        return super().form_valid(form)
