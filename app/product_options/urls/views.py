from django.urls import path
from .. import views

app_name = 'product_option'
urlpatterns = [
    path('<int:pk>', views.product_option_list, name='product-option'),
    path('create/', views.product_option_create, name='product_option-create')

]
