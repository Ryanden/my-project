from django.shortcuts import render

from ..models import Product

__all__ = (
    'product_list',
)


def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'products/product_list.html', context)
