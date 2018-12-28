from django.urls import path
from .. import views

app_name = 'bookmark'
urlpatterns = [
    path('recipe_create/', views.bookmark_create, name='bookmark-create'),
]
