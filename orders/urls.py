from django.urls import path

from orders.views import MyOrderView, CreateOrderBookView, DeleteOrderBookView

urlpatterns = [
    path('my-order', MyOrderView.as_view(), name='my_order'),
    path('add-order', CreateOrderBookView.as_view(), name='add_order'),
    path('delete-order-book/<int:pk>', DeleteOrderBookView.as_view(), name='delete_order_book'),
]
