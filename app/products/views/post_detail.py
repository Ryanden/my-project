from django.shortcuts import render

from ..models import Product, Comment

__all__ = (
    'product_detail',
)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    comment = Comment.objects.filter(product=product)
    context = {
        'product': product,
        'comments': comment,
    }
    return render(request, 'products/product_detail.html', context)
