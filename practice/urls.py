from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('goal/<int:pk>/', views.goal_detail, name='goal_detail'),
    path('goal/new/', views.goal_create, name='create_goal'),
    path('session/new/', views.session_create, name='create_session'),
    path('session/<int:pk>/', views.session_detail, name='session_detail'),
    path('goal/<int:goal_id>/session/new/', views.session_create_for_goal, name='create_session_for_goal'),
]
