from django.urls import path
from .. import views

app_name = 'lectures'
urlpatterns = [
    path('<int:pk>', views.product_list, name='lecture')
]
