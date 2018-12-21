from django.urls import path

from .. import apis

urlpatterns = [
    path('', apis.UserList.as_view()),
    path('signup/', apis.UserCreate.as_view()),
    path('<int:pk>/', apis.UserDetail.as_view()),
    path('signin/', apis.AuthToken.as_view()),
    path('auth-test/', apis.AuthenticationTest.as_view()),
    path('facebook-auth-token/', apis.FacebookAuthToken.as_view()),
    path('profile/', apis.Profile.as_view()),
]
