from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from costcalculator.forms import CalculatorForm
from costcalculator.models import CostCalculator, Item

__all__ = (
    'calculator',
)


@login_required
def calculator(request):
    ingredients = CostCalculator.objects.filter(user=request.user)

    items = Item.objects.filter(user=request.user)

    cost = 0

    for product in request.user.calculators.filter(user=request.user):
        cost += product.ingredient.cost_per_one * product.usage

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
        'ingredients': ingredients,
        'cost': cost,
        'items': items,
    }
    return render(request, 'calculator/calculator.html', context)
