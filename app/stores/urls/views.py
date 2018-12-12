from django.urls import path

from .. import views

app_name = 'store'

urlpatterns = [
    path('create/', views.store_create, name='store-create'),
    path('<str:name>/', views.store_home, name='store-home'),

]
