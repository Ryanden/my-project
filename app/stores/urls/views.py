from django.urls import path

from .. import views

app_name = 'stores'
urlpatterns = [
    # config.urls
    #  path('stores/', include(이 urlpatterns))
    path('', views.store_list, name='store-list'),
    path('tags/<str:tag>/', views.search_store_list, name='search-store-list'),
    path('<int:pk>/', views.store_detail, name='store-detail'),
    path('<int:pk>/delete/', views.store_delete, name='store-delete'),
    path('<int:pk>/like/', views.store_like, name='store-like'),
    path('<int:pk>/dislike/', views.store_dislike, name='store-dislike'),
    path('create/', views.store_create, name='store-create'),
    path('<int:store_pk>/comment/create/',
         views.comment_create,
         name='comment-create'),
    path('<int:store_pk>/comment/<int:comment_pk>/create/',
         views.comment_create,
         name='child-comment-create'),
]
