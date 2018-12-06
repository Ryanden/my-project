from django.urls import path

from .. import apis

urlpatterns = [
    path('', apis.LectureList.as_view()),
    path('<int:pk>/', apis.LectureDetail.as_view()),
]
