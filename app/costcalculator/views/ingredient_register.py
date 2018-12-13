from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from ..forms import IngredientForm

__all__ = (
    'ingredient_register',
)


def ingredient_register(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            ingredient = form.register()
            ingredient.cost_per_one = int(ingredient.cost) / int(ingredient.capacity)
            ingredient.save()
            print('등록성공')

            return redirect('costcalculator:calculator-menu')
    else:
        form = IngredientForm()
    context = {
        'form': form,
    }
    return render(request, 'calculator/ingredient_register.html', context)

#
# @login_required
# def product_create_with_form(request):
#     if request.method == 'POST':
#         form = StoreForm(request.POST, request.FILES)
#         if form.is_valid():
#             product = form.save(author=request.user)
#             return redirect('products:product-detail', pk=product.pk)
#     else:
#         form = StoreForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'products/product_create.html', context)
