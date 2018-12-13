from django.urls import path
from .. import views

app_name = 'costcalculator'
urlpatterns = [
    path('', views.calculator, name='calculator'),
    path('menu/', views.ingredient_list, name='calculator-menu'),
    path('ingredient_register/', views.ingredient_register, name='ingredient-register'),
    path('ingredient_delete/<int:pk>', views.ingredient_delete, name='ingredient-delete'),
    path('item_ingredient_delete/<int:pk>', views.item_ingredient_delete, name='item-ingredient-delete'),
    path('item/<int:pk>', views.item_detail, name='item-detail'),
    path('item_create/', views.item_create, name='item-create'),
    path('item_register/<int:pk>', views.item_register, name='item-register'),
    path('item_delete/<int:pk>', views.item_delete, name='item-delete'),

]
