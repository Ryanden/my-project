from django.shortcuts import render


def index(request):
    # TEMPLATE 설정 app/template 추

    print('메인페이지')

    context = {
        'products': 'aa'
    }

    return render(request, 'production/product-list.html', context)
