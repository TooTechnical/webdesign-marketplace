from django.shortcuts import redirect
from django.views.generic import ListView
from .models import CartItem

class CartView(ListView):
    model = CartItem
    template_name = 'cart/cart.html'
    context_object_name = 'cart_items'

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)

def add_to_cart(request, product_id=None, service_id=None):
    if product_id:
        CartItem.objects.create(user=request.user, product_id=product_id)
    elif service_id:
        CartItem.objects.create(user=request.user, service_id=service_id)
    return redirect('cart')
