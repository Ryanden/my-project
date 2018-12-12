from django.shortcuts import render
from product_options.models import ProductOption


def product_option_list(request, pk):
    product_option = ProductOption.objects.filter(post=pk)

    print(product_option)

    # print(product_option.product_name)

    context = {

        'product_options': product_option
    }

    return render(request, 'product/product-product_option.html', context)
