from django.db.models import Q
from django.views.generic import ListView
from .models import Product, Service

class ProductSearchView(ListView):
    template_name = 'products/search.html'
    context_object_name = 'results'

    def get_queryset(self):
        query = self.request.GET.get('q')
        category = self.request.GET.get('category')
        
        if query:
            products = Product.objects.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )
            services = Service.objects.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )
            if category:
                products = products.filter(category=category)
                services = services.filter(category=category)
            return list(products) + list(services)
        return Product.objects.none()
