from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST

from ..models import Product

__all__ = (
    'product_like',
    'product_dislike',
    'product_like_toggle',
)


@login_required
@require_POST
def product_like(request, pk):
    product = get_object_or_404(Product, pk=pk)
    request.user.like_posts.add(product)
    return redirect('products:product-detail', pk=pk)


@login_required
@require_POST
def product_dislike(request, pk):
    product = get_object_or_404(Product, pk=pk)
    request.user.like_posts.remove(product)
    return redirect('products:product-detail', pk=pk)


@login_required
@require_POST
def product_like_toggle(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.user.like_posts.filter(post=product).exists():
        request.user.like_posts.remove(product)
    else:
        request.user.like_posts.add(product)
    return redirect('products:product-detail', pk=pk)
