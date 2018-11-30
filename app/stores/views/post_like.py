from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST

from ..models import Store

__all__ = (
    'store_like',
    'store_dislike',
    'store_like_toggle',
)


@login_required
@require_POST
def store_like(request, pk):
    store = get_object_or_404(Store, pk=pk)
    request.user.like_posts.add(store)
    return redirect('stores:store-detail', pk=pk)


@login_required
@require_POST
def store_dislike(request, pk):
    store = get_object_or_404(Store, pk=pk)
    request.user.like_posts.remove(store)
    return redirect('stores:store-detail', pk=pk)


@login_required
@require_POST
def store_like_toggle(request, pk):
    store = get_object_or_404(Store, pk=pk)
    if request.user.like_posts.filter(post=store).exists():
        request.user.like_posts.remove(store)
    else:
        request.user.like_posts.add(store)
    return redirect('stores:store-detail', pk=pk)
