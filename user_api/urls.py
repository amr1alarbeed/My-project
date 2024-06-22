from django.urls import path
from user_api.views import (
    UserRegister,
    UserLogin,
    UserLogout,
    UserView,
)

urlpatterns = [
    path('user/register', UserRegister.as_view(), name='register'),
    path('user/login', UserLogin.as_view(), name='login'),
    path('user/logout', UserLogout.as_view(), name='logout'),
    path('user', UserView.as_view(), name='user'),
]
