from django.shortcuts import render

from costcalculator.models import ItemRegister

__all__ = (
    'item_list',
)


def item_list(request):
    items = ItemRegister.objects.all()

    context = {
        'items': items,
    }
    return render(request, 'calculator/calculator_menu.html', context)
