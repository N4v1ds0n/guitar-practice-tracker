from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Goal, PracticeSession, StandardGoalDefinition, StandardPracticeSession

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'goal_type', 'is_complete', 'target_date')
    list_filter = ('goal_type',)
    search_fields = ('title', 'user__username')

@admin.register(PracticeSession)
class PracticeSessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'goal', 'date', 'duration', 'tempo', 'accuracy')
    list_filter = ('date', 'goal')
    search_fields = ('user__username', 'goal__title')

@admin.register(StandardGoalDefinition)
class StandardGoalDefinitionAdmin(admin.ModelAdmin):
    list_display = ('name', 'goal_type')
    list_filter = ('goal_type',)
    search_fields = ('name',)

@admin.register(StandardPracticeSession)
class StandardPracticeSessionAdmin(admin.ModelAdmin):
    list_display = ('name', 'goal_type')
    list_filter = ('goal_type',)
    search_fields = ('name',)
