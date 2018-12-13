from django.urls import path

from .. import apis

urlpatterns = [
    path('', apis.OrderList.as_view()),
    path('<int>pk/', apis.OrderDetail.as_view()),
    path('create/', apis.OrderCreate.as_view()),
]
