from django.urls import path

from .. import apis

urlpatterns = [
    path('', apis.QualityTestList.as_view()),
    path('<int:pk>/', apis.QualityTestDetail.as_view()),
    path('create/', apis.QualityTestCreate.as_view()),
    path('institution/', apis.TestInstitutionList.as_view()),
]
