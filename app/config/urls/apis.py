from django.urls import path, include

urlpatterns = [

    path('members/', include('members.urls.apis')),
    path('posts/', include('posts.urls.apis')),
]
