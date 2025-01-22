import stripe
from django.conf import settings
from django.views.generic import View
from django.shortcuts import redirect
from cart.models import CartItem

stripe.api_key = settings.STRIPE_SECRET_KEY

class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        cart_items = CartItem.objects.filter(user=request.user)
        line_items = []
        for item in cart_items:
            if item.product:
                line_items.append({
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': int(item.product.price * 100),
                        'product_data': {
                            'name': item.product.name,
                        },
                    },
                    'quantity': item.quantity,
                })
            elif item.service:
                line_items.append({
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': int(item.service.price * 100),
                        'product_data': {
                            'name': item.service.name,
                        },
                    },
                    'quantity': 1,
                })

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url=request.build_absolute_uri('/checkout/success/'),
            cancel_url=request.build_absolute_uri('/checkout/cancel/'),
        )
        return redirect(checkout_session.url)
