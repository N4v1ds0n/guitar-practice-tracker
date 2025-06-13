from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('goals/', views.goals_list, name='goals_list'),
    path('goals/new/', views.goal_create, name='goal_create'),
    path('goals/<int:pk>/', views.goal_detail, name='goal_detail'),
    path('sessions/new/', views.session_create, name='session_create'),
]
