from django.urls import path

from .. import apis

urlpatterns = [
    path('', apis.ProductOptionList.as_view()),
    path('<int:pk>/', apis.ProductOptionDetail.as_view()),
    path('create/', apis.ProductOptionCreate.as_view()),
]
