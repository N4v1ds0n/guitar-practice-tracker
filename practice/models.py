from django.db import models
from django.db.models import JSONField
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

    # Metrics config
    metrics = JSONField(
        null=True,
        blank=True,
        help_text='Dict of target values for selected metrics (e.g. {"tempo": 120, "mistakes": 0, "duration": 300})'
    )
    start_tempo = models.PositiveIntegerField(null=True, blank=True)

    def is_standard(self):
        return self.standard_goal is not None

    def get_metrics(self):
        if self.is_standard():
            return self.standard_goal.metrics
        return list(self.metrics.keys()) if self.metrics else []

    def get_target_for(self, metric):
        if self.is_standard():
            return self.standard_goal.metrics.get(metric)
        return self.metrics.get(metric) if self.metrics else None

    def get_progress(self):
        """
        Returns progress for each tracked metric as a percentage.
        """
        sessions = self.sessions.all()
        progress = {}

        for metric in self.get_metrics():
            target = self.get_target_for(metric)
            if not target:
                progress[metric] = 0
                continue

            if metric == "tempo":
                latest = max([s.tempo for s in sessions if s.tempo], default=self.start_tempo or 0)
                base = self.start_tempo or 0
                progress[metric] = min(100, round(((latest - base) / (target - base)) * 100, 2)) if target > base else 0

            elif metric == "duration":
                total = sum([s.duration for s in sessions])
                progress[metric] = min(100, round((total / target) * 100, 2))

            elif metric == "mistakes":
                if not sessions:
                    progress[metric] = 0
                else:
                    success_sessions = [s for s in sessions if s.mistakes is not None and s.mistakes <= target]
                    progress[metric] = round((len(success_sessions) / len(sessions)) * 100, 2)

            else:
                # Generic metric fallback
                total = sum([getattr(s, metric, 0) or 0 for s in sessions])
                progress[metric] = min(100, round((total / target) * 100, 2))

        return progress

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
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Session on {self.date.date()} for goal '{self.goal}'"

