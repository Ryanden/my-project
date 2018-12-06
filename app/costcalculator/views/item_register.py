from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from ..forms import ItemRegisterModelForm, ItemRegisterForm

__all__ = (
    'item_register',
)


def item_register(request):

    if request.method == 'POST':
        form = ItemRegisterModelForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            # item.author = request.user
            item.cost_per_one = item.cost / item.capacity
            print('등록성공')
            item.save()
            return redirect('costcalculator:calculator_menu')
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

