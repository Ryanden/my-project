from django.shortcuts import render

from ..models import Store

__all__ = (
    'store_list',
)


def store_list(request):
    stores = Store.objects.all()
    context = {
        'stores': stores,
    }
    return render(request, 'stores/store_list.html', context)
