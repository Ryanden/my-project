from django.urls import path

from .. import apis

urlpatterns = [
    path('', apis.CostCalculatorList.as_view()),
    path('<int:pk>/', apis.CostCalculatorDetail.as_view()),
    path('create/', apis.CostCalculatorCreate.as_view()),
    path('info/', apis.CostCalculatorInfoList.as_view()),
    path('item/', apis.ItemList.as_view()),
    path('item/<int:pk>/', apis.ItemDetail.as_view()),
    path('item/create/', apis.ItemCreate.as_view()),
    path('material/', apis.MaterialList.as_view()),
    path('material/<int:pk>/', apis.MaterialDetail.as_view()),
    path('material/create/', apis.MaterialCreate.as_view()),
]
