from django.urls import path
from .. import views

app_name = 'costcalculator'
urlpatterns = [
    path('', views.calculator, name='calculator'),
    path('menu/', views.material_list, name='calculator-menu'),
    path('material_register/', views.material_register, name='material-register'),
    path('material_delete/<int:pk>', views.material_delete, name='material-delete'),
    path('item_material_delete/<int:pk>', views.item_material_delete, name='item-material-delete'),
    path('item/<int:pk>', views.item_detail, name='item-detail'),
    path('item_create/', views.item_create, name='item-create'),
    path('item_register/<int:pk>', views.item_register, name='item-register'),
    path('item_delete/<int:pk>', views.item_delete, name='item-delete'),

]
