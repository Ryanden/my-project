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
# def product_create_with_form(request):
#     if request.method == 'POST':
#         form = StoreForm(request.POST, request.FILES)
#         if form.is_valid():
#             product = form.save(author=request.user)
#             return redirect('products:product-detail', pk=product.pk)
#     else:
#         form = StoreForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'products/product_create.html', context)
