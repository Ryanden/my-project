from django.shortcuts import render

from costcalculator.models import ItemRegister, Recipe

__all__ = (
    'item_list',
)


def item_list(request):
    items = ItemRegister.objects.all()

    recipes = Recipe.objects.all()

    context = {
        'items': items,
        'recipes': recipes,
    }
    return render(request, 'calculator/calculator_menu.html', context)
