from django.urls import path

from .. import views

app_name = 'members'

urlpatterns = [
   path('login', views.login_view, name='login'),
   path('logout', views.logout_view, name='logout'),
   path('signup2', views.signup, name='signup2'),
   path('withdraw', views.withdraw, name='withdraw'),
]
