from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from ..forms import BookMarkForm

__all__ = (
    'bookmark_create',
)


def bookmark_create(request):
    if request.method == 'POST':
        form = BookMarkForm(request.POST)
        if form.is_valid():

            form.save(user=request.user)

            print('등록성공')

            return redirect('costcalculator:calculator-menu')
    else:
        form = BookMarkForm()
    context = {
        'form': form,
    }
    return render(request, 'calculator/item_create.html', context)

