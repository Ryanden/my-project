from django.urls import path
from .. import views

app_name = 'carts'
urlpatterns = [
    path('<int:pk>', views.product_option_list, name='cart')
]
