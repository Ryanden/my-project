from django.urls import path

from .. import apis

urlpatterns = [
    path('', apis.BookMarkList.as_view()),
    path('<int:pk>/', apis.BookMarkDetail.as_view()),
    path('create/', apis.BookMarkCreate.as_view()),
]
