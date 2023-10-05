from django.urls import path
from .views import *
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView

urlpatterns = [
    path('', index, name="index"),
    path('signup/', signup, name='signup'),
    path('index2/', index2, name='index2'),
    path('login/', user_login, name='login'),
    path('logout/', userLogout, name="logout"),
    path('adminreg/',adminreg,name="adminreg"),
    
    path('accounts/login/',user_login,name='login'),
    
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
