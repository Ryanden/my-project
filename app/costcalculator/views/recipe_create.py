from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from ..forms import RecipeForm

__all__ = (
    'recipe_create',
)


def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():

            form.save(user=request.user)

            print('등록성공')

            return redirect('costcalculator:calculator-menu')
    else:
        form = RecipeForm()
    context = {
        'form': form,
    }
    return render(request, 'calculator/recipe_create.html', context)

