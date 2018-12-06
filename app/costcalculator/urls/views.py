from django.urls import path
from .. import views

app_name = 'costcalculator'
urlpatterns = [
    path('', views.calculator, name='calculator'),
    path('menu/', views.item_list, name='calculator-menu'),
    path('register/', views.item_register, name='item-register'),
    # path('<int:pk>', views.cost_calculator, name='cost-calculator')
]