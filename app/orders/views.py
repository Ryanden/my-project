from django.shortcuts import render
from product_options.models import ProductOption


def product_list(request, pk):
    product = ProductOption.objects.filter(post=pk)

    print(product)

    # print(product.product_name)

    context = {

        'products': product
    }

    return render(request, 'product/product-product.html', context)
