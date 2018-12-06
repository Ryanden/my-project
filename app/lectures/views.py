from django.shortcuts import render
from products.models import Product


def product_list(request, pk):
    product = Product.objects.filter(post=pk)

    print(product)

    # print(product.product_name)

    context = {

        'products': product
    }

    return render(request, 'store/store-product.html', context)
