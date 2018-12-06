from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from costcalculator.forms import CalculatorForm
from costcalculator.models import ItemRegister, CostCalculator

__all__ = (
    'calculator',
)


@login_required
def calculator(request):
    items = CostCalculator.objects.filter(user=request.user)
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
        'items': items,
    }
    return render(request, 'calculator/calculator.html', context)
