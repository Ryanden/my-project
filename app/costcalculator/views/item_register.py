from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from costcalculator.forms import CalculatorForm
from costcalculator.models import Item, CostCalculator

__all__ = (
    'item_register',
)


@login_required
def item_register(request, pk):

    item = Item.objects.get(pk=pk)

    cost = 0

    for product in request.user.calculators.filter(user=request.user):
        cost += product.material.cost_per_one * product.usage

    item.prime_cost = cost

    item.margin = request.POST['margin']

    item.profit = request.POST['profit']

    item.save()

    return redirect('costcalculator:calculator-menu')
