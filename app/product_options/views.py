from django.shortcuts import render, redirect
from product_options.models import ProductOption
from products.models import Product


def product_option_list(request, pk):
    product_option = ProductOption.objects.filter(post=pk)

    print(product_option)

    # print(product_option.name)

    context = {

        'product_option': product_option
    }

    return render(request, 'product/product-product_option.html', context)


def product_option_create(request, pk):

    product = Product.objects.get(pk=pk)

    ProductOption.objects.create(
        name='a',
        description='a',
        product=product
    )

    return redirect('products:product-detail', pk)
