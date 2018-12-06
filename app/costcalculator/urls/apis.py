from django.urls import path

from .. import apis

urlpatterns = [
    path('', apis.CostCalculatorList.as_view()),
    path('<int:pk>/', apis.CostCalculatorDetail.as_view()),
]
