from django.urls import path

from .. import apis

urlpatterns = [
    path('', apis.UserList.as_view()),
    path('create/', apis.UserCreate.as_view()),
    path('<int:pk>/', apis.UserDetail.as_view()),
    path('patch/<int:pk>/', apis.UserPatch.as_view()),
    path('delete/<int:pk>/', apis.UserDelete.as_view()),
    path('sign_in/', apis.AuthToken.as_view()),
    path('auth-test/', apis.AuthenticationTest.as_view()),
    path('facebook-auth-token/', apis.FacebookAuthToken.as_view()),
    path('profile/', apis.Profile.as_view()),
]
