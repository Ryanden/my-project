from django.urls import path

from .. import views

app_name = 'products'
urlpatterns = [
    # config.urls
    #  path('products/', include(이 urlpatterns))
    path('', views.product_list, name='product-list'),
    path('tags/<str:tag>/', views.search_product_list, name='search-product-list'),
    path('<int:pk>/', views.product_detail, name='product-detail'),
    path('<int:pk>/delete/', views.product_delete, name='product-delete'),
    path('<int:pk>/like/', views.product_like, name='product-like'),
    path('<int:pk>/dislike/', views.product_dislike, name='product-dislike'),
    path('create/', views.product_create, name='product-create'),
    path('<int:product_pk>/comment/create/',
         views.comment_create,
         name='comment-create'),
    path('<int:product_pk>/comment/<int:comment_pk>/create/',
         views.comment_create,
         name='child-comment-create'),
]
