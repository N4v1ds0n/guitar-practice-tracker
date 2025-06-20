from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import CustomAuthenticationForm



urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(
        template_name='accounts/login.html',
        authentication_form=CustomAuthenticationForm
    ), name='login'),
    path(
        'logout/',
        views.custom_logout, name='logout'
        ),
    path('profile/', views.profile, name='profile'),
    path('account/delete/', views.delete_account, name='delete_account'),
]

