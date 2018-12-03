from django.urls import path
from .. import views

app_name = 'orders'
urlpatterns = [
    path('<int:pk>', views.product_list, name='product')
]
