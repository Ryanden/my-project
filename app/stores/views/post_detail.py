from django.shortcuts import render

from ..models import Store

__all__ = (
    'store_detail',
)


def store_detail(request, pk):
    store = Store.objects.get(pk=pk)
    context = {
        'store': store,
    }
    return render(request, 'stores/store_detail.html', context)
