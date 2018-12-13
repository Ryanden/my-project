from django.shortcuts import render

from costcalculator.models import Ingredient, Item

__all__ = (
    'ingredient_list',
)


def ingredient_list(request):
    ingredients = Ingredient.objects.all()

    items = Item.objects.all()

    context = {
        'ingredients': ingredients,
        'items': items,
    }
    return render(request, 'calculator/calculator_menu.html', context)
