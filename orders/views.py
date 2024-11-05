from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
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


class DeleteOrderBookView(LoginRequiredMixin, View):
    def post(self, request, pk):
        order_book = get_object_or_404(OrderBook, pk=pk, order__user=request.user, order__status=True)
        order_book.delete()
        messages.success(request, "Book removed from the order.", extra_tags='bg-green-500')
        return HttpResponseRedirect(reverse_lazy('my_order'))
