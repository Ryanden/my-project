from django.urls import path
from .. import views

app_name = 'products'
urlpatterns = [
    path('', views.store_list, name='store-list'),
    path('<int:pk>', views.product_list, name='product')
]
