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
    if request.method == 'POST':
        name = request.POST['name']

        description = request.POST['description']

        price = int(request.POST['price'])

        count = int(request.POST['count'])

        product = Product.objects.get(pk=request.POST['product'])

        ProductOption.objects.create(
            name=name,
            description=description,
            price=price,
            count=count,
            product=product,
        )

        return redirect('store:store-home', request.user)

    return render(request, 'products/product_option_create.html', pk)
