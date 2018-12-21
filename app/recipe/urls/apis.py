from django.urls import path

from .. import apis

urlpatterns = [
    path('', apis.RecipeList.as_view()),
    path('<int:pk>/', apis.RecipeDetail.as_view()),
    path('create/', apis.RecipeCreate.as_view()),
]
