from django.urls import path

from .. import apis

urlpatterns = [
    path('', apis.QualityTestList.as_view()),
    path('<int:pk>/', apis.QualityTestDetail.as_view()),
    path('create/', apis.QualityTestCreate.as_view()),
    path('patch/<int:pk>/', apis.QualityTestPatch.as_view()),
    path('delete/<int:pk>/', apis.QualityTestDelete.as_view()),
    path('institution/', apis.TestInstitutionList.as_view()),
    path('institution/create/', apis.TestInstitutionCreate.as_view()),
]
