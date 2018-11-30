from django.urls import path

from .. import apis

urlpatterns = [
    path('', apis.ProductList.as_view()),
    path('<int:pk>/', apis.ProductDetail.as_view()),
    path('ordering/', apis.OrderingList.as_view()),
    path('orderinginfo/', apis.OrderingInfoList.as_view()),
]
