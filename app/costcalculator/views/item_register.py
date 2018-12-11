from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from ..forms import ItemRegisterForm

__all__ = (
    'item_register',
)


def item_register(request):
    if request.method == 'POST':
        form = ItemRegisterForm(request.POST)
        if form.is_valid():
            item = form.register()
            item.cost_per_one = int(item.cost) / int(item.capacity)
            item.save()
            print('등록성공')

            return redirect('costcalculator:calculator-menu')
    else:
        form = ItemRegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'calculator/item_register.html', context)

#
# @login_required
# def store_create_with_form(request):
#     if request.method == 'POST':
#         form = StoreForm(request.POST, request.FILES)
#         if form.is_valid():
#             store = form.save(author=request.user)
#             return redirect('stores:store-detail', pk=store.pk)
#     else:
#         form = StoreForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'stores/store_create.html', context)
