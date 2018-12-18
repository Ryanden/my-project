from django.urls import path, include

urlpatterns = [

    path('members/', include('members.urls.apis')),
    path('products/', include('products.urls.apis')),
    path('options/', include('product_options.urls.apis')),
    path('lectures/', include('lectures.urls.apis')),
    path('carts/', include('shopping_carts.urls.apis')),
    path('orders/', include('orders.urls.apis')),
    path('calculator/', include('costcalculator.urls.apis')),
    path('recipe/', include('recipe.urls.apis')),
    path('quality_test/', include('quality_test.urls.apis')),
]
