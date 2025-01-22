from django.urls import path
from .views import CartView, add_to_cart

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('add/<int:product_id>/', add_to_cart, name='add_product_to_cart'),
    path('add/service/<int:service_id>/', add_to_cart, name='add_service_to_cart'),
]
