from django.urls import path
from .. import views

app_name = 'ingredient'
urlpatterns = [
    path('ingredient_create/', views.ingredients_create, name='ingredient-create'),
]
