from django.urls import path

from userextends import views

urlpatterns = [
    path('user_create/', views.UserCreateView.as_view(), name='user-create'),
    path('update_user/', views.update_user, name='user-update'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('update_info/', views.update_info, name='update-info'),
    path('update_password/', views.update_password, name='update-password')
]