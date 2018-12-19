from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from ..forms import MaterialForm

__all__ = (
    'material_register',
)


def material_register(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            material = form.register()
            material.cost_per_one = int(material.cost) / int(material.capacity)
            material.save()
            print('등록성공')

            return redirect('costcalculator:calculator-menu')
    else:
        form = MaterialForm()
    context = {
        'form': form,
    }
    return render(request, 'calculator/material_register.html', context)

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
