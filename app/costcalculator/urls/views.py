from django.urls import path
from .. import views

app_name = 'costcalculator'
urlpatterns = [
    path('', views.calculator, name='calculator'),
    path('menu/', views.item_list, name='calculator-menu'),
    path('item_register/', views.item_register, name='item-register'),
    path('item_delete/<int:pk>', views.item_delete, name='item-delete'),
    path('recipe_material_delete/<int:pk>', views.recipe_material_delete, name='recipe-material-delete'),
    path('recipe/<int:pk>', views.recipe_detail, name='recipe-detail'),
    path('recipe_create/', views.recipe_create, name='recipe-create'),
    path('recipe_register/<int:pk>', views.recipe_register, name='recipe-register'),
    path('recipe_delete/<int:pk>', views.recipe_delete, name='recipe-delete'),

]
