from django.shortcuts import render

from ..models import Store

__all__ = (
    'search_store_list',
)


def search_store_list(request, tag):
    stores = Store.objects.filter(tags__name=tag).distinct()
    context = {
        'stores': stores,
    }
    return render(request, 'stores/search_store_list.html', context)
