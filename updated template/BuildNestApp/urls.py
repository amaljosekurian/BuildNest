from django.urls import path
from .views import *
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView

urlpatterns = [
    path('', index, name="index"),
    path('signup/', signup, name='signup'),
    path('index2/', index2, name='index2'),
    path('user_login/', user_login, name='user_login'),
    path('logout/', logout, name="logout"),
    path('adminreg/',adminreg,name="adminreg"),
    path('accounts/login/',user_login,name='login'), 
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('toggle-active/<int:user_id>/<str:is_active>/',toggle_active, name='toggle_active'),
    path('contractor/', contractor, name='contractor'),
    path('client/', client, name='client'),
    path('purchase_manager/', purchase_manager, name='purchase_manager'),
    path('user_profile/', user_profile, name="user_profile"),
    path('update_user_details/', update_user_details, name="update_user_details"),

    # path('contractor_dashboard/', contractor_dashboard, name='contractor_dashboard'),

    
    # path('delAdmin/', delAdmin, name='delAdmin')

]
