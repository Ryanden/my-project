from django.urls import path
from .. import views

app_name = 'quality_test'
urlpatterns = [
    path('quality_test_create/', views.quality_test_create, name='quality_test-create'),
]
