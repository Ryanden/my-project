from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from products.models import Product


def store_home(request, name):
    product = Product.objects.filter(author=request.user)

    context = {
        'products': product,

    }

    return render(request, 'stores/store_home.html', context)


def store_create(request):
    # user_store = Store.objects.filter(user=request.user)
    #
    # if request.method == 'POST':
    #     name = request.POST['name']
    #
    #     store = Store.objects.create(
    #         user=request.user,
    #         name=name,
    #     )
    #
    #     context = {
    #
    #         'stores': store,
    #     }
    #     return render(request, 'stores/store_home.html', context)
    #
    # context = {
    #
    #     'user_store': user_store,
    # }
    #
    # return render(request, 'stores/store_create.html', context)
    return HttpResponse('aa')
