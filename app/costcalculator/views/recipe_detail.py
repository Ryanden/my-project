from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from costcalculator.forms import CalculatorForm
from costcalculator.models import Recipe, CostCalculator

__all__ = (
    'recipe_detail',
)


@login_required
def recipe_detail(request, pk):
    materials = CostCalculator.objects.filter(user=request.user)

    recipes = Recipe.objects.filter(pk=pk)

    cost = 0

    for product in request.user.calculators.filter(user=request.user):
        cost += product.item.cost_per_one * product.usage

    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            print('성공')

            form.save(user=request.user)

            return redirect('costcalculator:recipe-detail', pk)
    else:
        form = CalculatorForm()

    context = {
        'form': form,
        'materials': materials,
        'cost': cost,
        'recipes': recipes,
    }
    return render(request, 'calculator/recipe_detail.html', context)



#
# @login_required
# def recipe_cre(request):
#     recipe = 0
#
#     if request.method == 'POST':
#         recipe_name = request.POST.get('name')
#
#         recipe_price = request.POST.get('price')
#         recipe_prime_cost = request.POST.get('prime-cost')
#         recipe_margin = request.POST.get('margin')
#         recipe_profit = request.POST.get('profit')
#
#         Recipe.objects.create(
#             user=request.user,
#             name=recipe_name,
#             price=recipe_price,
#             prime_cost=recipe_prime_cost,
#             margin=float(recipe_margin),
#             profit=recipe_profit
#         )
#
#         return redirect('costcalculator:calculator')
#     context = {
#         'recipe': recipe,
#     }
#
#     return render(request, 'calculator/calculator.html', context)
