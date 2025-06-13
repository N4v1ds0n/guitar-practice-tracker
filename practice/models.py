from django.db import models
from django.conf import settings
from django.utils import timezone
from accounts.models import CustomUser as User

# Create your models here.

# Model for standard goals that users can set but not adjust


class StandardGoalDefinition(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    metrics = models.JSONField(
        help_text='''List of metrics this goal tracks,
        e.g. ['tempo', 'mistakes', 'duration']'''
        )

    CATEGORY_CHOICES = [
        ('technique', 'Technique'),
        ('theory', 'Theory'),
        ('ear_training', 'Ear Training'),
        ('repertoire', 'Repertoire'),
        ('other', 'Other'),
    ]
    category = models.CharField(
        max_length=50, choices=CATEGORY_CHOICES, default='other')

    def __str__(self):
        return self.name
    
    
# Model for Goals that users can set and track

class Goal(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, related_name='goals'
    )
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    standard_goal = models.ForeignKey(
        StandardGoalDefinition,
        on_delete=models.SET_NULL, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    target_date = models.DateField(null=True, blank=True)

    def is_standard(self):
        return self.standard_goal is not None

    def __str__(self):
        return self.title

# Model for a practice session


class PracticeSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal = models.ForeignKey(
                            Goal,
                            on_delete=models.SET_NULL,
                            null=True,
                            blank=True,
                            related_name='sessions'
        )
    date = models.DateTimeField(default=timezone.now)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    tempo = models.PositiveIntegerField(null=True, blank=True)
    mistakes = models.PositiveIntegerField(null=True, blank=True)
    accuracy = models.FloatField(null=True, blank=True)
    progress_percent = models.FloatField(null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Session on {self.date.date()} for goal '{self.goal}'"
