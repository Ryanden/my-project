from django.shortcuts import render
from products.models import Store, Product


def store_list(request):
    stores = Store.objects.all()
    context = {

        'stores': stores
    }

    return render(request, 'store/store-list.html', context)


def product_list(request, pk):
    product = Product.objects.filter(store=pk)

    print(product)

    # print(product.product_name)

    context = {

        'products': product
    }

    return render(request, 'store/store-product.html', context)

def product_create(request):
    pass