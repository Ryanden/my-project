from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from costcalculator.forms import CalculatorForm
from costcalculator.models import Recipe, CostCalculator

__all__ = (
    'recipe_register',
)


@login_required
def recipe_register(request, pk):

    recipe = Recipe.objects.get(pk=pk)

    cost = 0

    for product in request.user.calculators.filter(user=request.user):
        cost += product.item.cost_per_one * product.usage

    recipe.prime_cost = cost

    recipe.margin = request.POST['margin']

    recipe.profit = request.POST['profit']

    recipe.save()

    return redirect('costcalculator:calculator-menu')
