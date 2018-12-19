from django.urls import path

from .. import apis

urlpatterns = [
    path('', apis.IngredientsLabelingList.as_view()),
    path('<int:pk>/', apis.IngredientsLabelingDetail.as_view()),
    path('create/', apis.IngredientsLabelingCreate.as_view()),
    path('patch/<int:pk>/', apis.IngredientsLabelingPatch.as_view()),
    path('delete/<int:pk>/', apis.IngredientsLabelingDelete.as_view()),

    path('ingredient/', apis.IngredientList.as_view()),
    path('ingredient/<int:pk>/', apis.IngredientDetail.as_view()),
    path('ingredient/create/', apis.IngredientCreate.as_view()),
    path('ingredient/patch/<int:pk>/', apis.IngredientPatch.as_view()),
    path('ingredient/delete/<int:pk>/', apis.IngredientDelete.as_view()),
]
