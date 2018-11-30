from django.urls import path

from .. import apis

urlpatterns = [
    path('', apis.StoreList.as_view()),
    path('<int:pk>/', apis.StoreDetail.as_view()),
]
