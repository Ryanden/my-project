from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from costcalculator.forms import CalculatorForm
from costcalculator.models import Item, CostCalculator

__all__ = (
    'item_detail',
)


@login_required
def item_detail(request, pk):
    materials = CostCalculator.objects.filter(user=request.user)

    items = Item.objects.filter(pk=pk)

    cost = 0

    for product in request.user.calculators.filter(user=request.user):
        cost += product.material.cost_per_one * product.usage

    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            print('성공')

            form.save(user=request.user)

            return redirect('costcalculator:item-detail', pk)
    else:
        form = CalculatorForm()

    context = {
        'form': form,
        'materials': materials,
        'cost': cost,
        'items': items,
    }
    return render(request, 'calculator/item_detail.html', context)



#
# @login_required
# def item_cre(request):
#     item = 0
#
#     if request.method == 'POST':
#         item_name = request.POST.get('name')
#
#         item_price = request.POST.get('price')
#         item_prime_cost = request.POST.get('prime-cost')
#         item_margin = request.POST.get('margin')
#         item_profit = request.POST.get('profit')
#
#         Item.objects.create(
#             user=request.user,
#             name=item_name,
#             price=item_price,
#             prime_cost=item_prime_cost,
#             margin=float(item_margin),
#             profit=item_profit
#         )
#
#         return redirect('costcalculator:calculator')
#     context = {
#         'item': item,
#     }
#
#     return render(request, 'calculator/calculator.html', context)
