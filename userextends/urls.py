from django.urls import path

from userextends import views

urlpatterns = [
    path('user_create/', views.UserCreateView.as_view(), name='user-create')
]