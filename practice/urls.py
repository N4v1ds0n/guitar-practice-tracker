from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('about', views.about, name='about'),
    path('goal/<int:pk>/', views.goal_detail, name='goal_detail'),
    path('goal/new/', views.goal_create, name='create_goal'),
    path('session/new/', views.session_create, name='create_session'),
    path('session/<int:pk>/', views.session_detail, name='session_detail'),
    path('goal/<int:goal_id>/session/new/',
         views.session_create_for_goal,
         name='create_session_for_goal'),
    path('api/standard-goal/',
         views.get_standard_goal_description,
         name='standard_goal_description'),
    path('goal/<int:pk>/delete/', views.goal_delete, name='goal_delete'),
    path('session/<int:pk>/delete/',
         views.session_delete, name='session_delete'),
    path('goals/<int:pk>/edit/', views.goal_edit, name='goal_edit'),
    path('sessions/<int:pk>/edit/', views.session_edit, name='session_edit'),
]
