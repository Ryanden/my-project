from django.urls import path

from .. import apis

urlpatterns = [
    path('', apis.CostCalculatorList.as_view()),
    path('<int:pk>/', apis.CostCalculatorDetail.as_view()),
    path('create/', apis.CostCalculatorCreate.as_view()),
    path('item/', apis.ItemList.as_view()),
    path('item/<int:pk>/', apis.ItemDetail.as_view()),
    path('item/create/', apis.ItemCreate.as_view()),
    path('ingredient/', apis.IngredientList.as_view()),
    path('ingredient/<int:pk>/', apis.IngredientDetail.as_view()),
    path('ingredient/create/', apis.IngredientCreate.as_view()),
]
