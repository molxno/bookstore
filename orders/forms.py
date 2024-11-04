from django.forms import ModelForm

from orders.models import OrderBook


class OrderBookForm(ModelForm):
    class Meta:
        model = OrderBook
        fields = ['book']
