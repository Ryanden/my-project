from django.urls import path, include

urlpatterns = [

    path('members/', include('members.urls.apis')),
    path('stores/', include('stores.urls.apis')),
    path('products/', include('products.urls.apis')),
    path('lectures/', include('lectures.urls.apis')),
    path('carts/', include('shopping_carts.urls.apis')),
    path('orders/', include('orders.urls.apis')),
]
