from django.shortcuts import render

from ..models import Store, Comment

__all__ = (
    'store_detail',
)


def store_detail(request, pk):
    store = Store.objects.get(pk=pk)
    comment = Comment.objects.filter(store=store)
    context = {
        'store': store,
        'comments': comment,
    }
    return render(request, 'stores/store_detail.html', context)
