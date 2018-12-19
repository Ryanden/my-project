from django.shortcuts import render

from costcalculator.models import Material, Item

__all__ = (
    'material_list',
)


def material_list(request):
    materials = Material.objects.all()

    items = Item.objects.all()

    context = {
        'materials': materials,
        'items': items,
    }
    return render(request, 'calculator/calculator_menu.html', context)
