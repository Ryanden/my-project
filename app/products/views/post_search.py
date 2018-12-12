from django.shortcuts import render

from ..models import Product

__all__ = (
    'search_product_list',
)


def search_product_list(request, tag):
    products = Product.objects.filter(tags__name=tag).distinct()
    context = {
        'products': products,
    }
    return render(request, 'products/search_product_list.html', context)
