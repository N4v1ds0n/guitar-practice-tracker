from django.db import models
from django.conf import settings
from django.utils import timezone
from accounts.models import CustomUser as User

GOAL_TYPE_CHOICES = [
    ('technique', 'Technique'),
    ('repertoire', 'Repertoire'),
    ('routine', 'Routine'),
    ('custom', 'Custom'),
]


class StandardGoalDefinition(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    goal_type = models.CharField(max_length=20, choices=GOAL_TYPE_CHOICES)

    def __str__(self):
        return self.name


class Goal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='goals')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    goal_type = models.CharField(max_length=20, choices=GOAL_TYPE_CHOICES, default='custom')
    standard_goal = models.ForeignKey(StandardGoalDefinition, on_delete=models.SET_NULL, null=True, blank=True)

    # Only for technique & custom
    target_tempo = models.PositiveIntegerField(null=True, blank=True)
    target_accuracy = models.FloatField(null=True, blank=True)
    target_duration = models.PositiveIntegerField(null=True, blank=True)  # in minutes

    # Only for routine
    routine_target_days = models.PositiveIntegerField(null=True, blank=True)  # e.g., 7 for perfect week

    created_at = models.DateTimeField(auto_now_add=True)
    target_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

    def is_complete(self):
        if self.goal_type == 'routine':
            return self.check_routine_completion()
        elif self.goal_type == 'repertoire':
            return False  # Manual completion
        return self.get_overall_progress() >= 100

    def get_overall_progress(self):
        sessions = self.sessions.all()
        if not sessions.exists():
            return 0

        progress = []

        if self.target_tempo:
            max_tempo = max([s.tempo or 0 for s in sessions])
            progress.append(min(1, max_tempo / self.target_tempo))

        if self.target_accuracy:
            max_acc = max([s.accuracy or 0 for s in sessions])
            progress.append(min(1, max_acc / self.target_accuracy))

        if self.target_duration:
            total_duration = sum([s.duration or 0 for s in sessions])
            progress.append(min(1, total_duration / self.target_duration))

        if not progress:
            return 0

        return round(sum(progress) / len(progress) * 100, 1)

    def check_routine_completion(self):
        sessions = self.sessions.filter(duration__gte=15).order_by('date')

        if not sessions.exists() or not self.routine_target_days:
            return False

        streak = 1
        for i in range(1, len(sessions)):
            delta = (sessions[i].date.date() - sessions[i - 1].date.date()).days
            if delta == 1:
                streak += 1
            elif delta > 1:
                streak = 1

            if streak >= self.routine_target_days:
                return True

        return False


class StandardPracticeSession(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    goal_type = models.CharField(max_length=20, choices=GOAL_TYPE_CHOICES, default='custom')

    def __str__(self):
        return self.name


class PracticeSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal = models.ForeignKey(Goal, on_delete=models.SET_NULL, null=True, blank=True, related_name='sessions')
    date = models.DateTimeField(default=timezone.now)

    # Core attributes used in custom/technical goals
    duration = models.PositiveIntegerField(help_text="Duration in minutes", null=True, blank=True)
    tempo = models.PositiveIntegerField(null=True, blank=True)
    accuracy = models.FloatField(null=True, blank=True, help_text="Accuracy as percentage (0–100)")

    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Session on {self.date.date()} for goal '{self.goal or 'Unlinked'}'"
