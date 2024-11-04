from django.urls import path

from orders.views import MyOrderView, CreateOrderBookView

urlpatterns = [
    path('my-order', MyOrderView.as_view(), name='my_order'),
    path('add-order', CreateOrderBookView.as_view(), name='add_order'),
]
