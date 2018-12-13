from django.urls import path

from .. import apis

urlpatterns = [
    path('', apis.CartList.as_view()),
    path('<int:pk>/', apis.CartDetail.as_view()),
    path('create/', apis.CartCreate.as_view()),
]
