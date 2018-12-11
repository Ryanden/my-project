from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from costcalculator.forms import CalculatorForm
from costcalculator.models import CostCalculator, Recipe

__all__ = (
    'calculator',
)


@login_required
def calculator(request):
    materials = CostCalculator.objects.filter(user=request.user)

    recipes = Recipe.objects.filter(user=request.user)

    cost = 0

    for product in request.user.calculators.filter(user=request.user):
        cost += product.item.cost_per_one * product.usage

    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            print('성공')

            form.save(user=request.user)

            return redirect('costcalculator:calculator')
    else:
        form = CalculatorForm()

    context = {
        'form': form,
        'materials': materials,
        'cost': cost,
        'recipes': recipes,
    }
    return render(request, 'calculator/calculator.html', context)
