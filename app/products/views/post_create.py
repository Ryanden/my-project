from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from ..forms import ProductModelForm, ProductForm
from ..models import Product

__all__ = (
    'product_create',
)


def product_create(request):
    # PostModelForm을 사용
    #  form = PostModelForm(request.POST, request.FILES)
    #  post = form.save(commit=False)
    #  post.author = request.user
    #  post.save()
    if request.method == 'POST':
        form = ProductModelForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.save()
            return redirect('products:product-detail', pk=product.pk)
    else:
        form = ProductModelForm()
    context = {
        'form': form,
    }
    return render(request, 'products/product_create.html', context)


@login_required
def product_create_with_form(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(author=request.user)
            return redirect('products:product-detail', pk=product.pk)
    else:
        form = ProductForm()
    context = {
        'form': form,
    }
    return render(request, 'products/product_create.html', context)


def product_create_without_form(request):
    if request.method == 'POST':
        product = Product(
            author=request.user,
            photo=request.FILES['photo'],
            content=request.POST['content'],
        )
        product.save()
        return redirect('products:product-detail', pk=product.pk)
    return render(request, 'products/product_create.html')
