from django.urls import path
from .views import UserRegistrationView, UserUpdateView, UserDeleteView , LoginView
from django.shortcuts import render
from .views import LoginView, login_view



urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('register/success/', lambda request: render(request, 'register_success.html'), name='user-register-success'),
    path('update/<uuid:user_id>/', UserUpdateView.as_view(), name='user-update'),
    path('update/success/', lambda request: render(request, 'update_success.html'), name='user-update-success'),
    path('delete/<uuid:user_id>/', UserDeleteView.as_view(), name='user-delete'),
    path('delete/success/', lambda request: render(request, 'delete_success.html'), name='user-delete-success'),
    # path('login/', LoginView.as_view(), name='login')
    path('login/', login_view, name='login'), 
    path('api/login/', LoginView.as_view(), name='api-login')
    
]
