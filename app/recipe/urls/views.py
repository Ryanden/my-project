from django.urls import path
from .. import views

app_name = 'recipe'
urlpatterns = [
    path('recipe_create/', views.recipe_create, name='recipe-create'),
]
