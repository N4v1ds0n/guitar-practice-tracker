from django import forms
from .models import Goal, PracticeSession


class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['title', 'description', 'standard_goal', 'target_date']

    # For custom goals: allow entry of selected metric values
    tempo = forms.IntegerField(required=False)
    mistakes = forms.IntegerField(required=False)
    duration = forms.IntegerField(required=False)

    def clean(self):
        cleaned_data = super().clean()

        # If it's a custom goal, gather the metrics
        if not cleaned_data.get('standard_goal'):
            metrics = {}
            for field in ['tempo', 'mistakes', 'duration']:
                val = cleaned_data.get(field)
                if val is not None:
                    metrics[field] = val
            cleaned_data['metrics'] = metrics

        return cleaned_data

    def save(self, commit=True):
        goal = super().save(commit=False)
        if not goal.standard_goal:
            goal.metrics = self.cleaned_data.get('metrics', {})
        if commit:
            goal.save()
        return goal


class PracticeSessionForm(forms.ModelForm):
    class Meta:
        model = PracticeSession
        fields = ['goal', 'duration', 'tempo', 'mistakes', 'accuracy', 'notes']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['goal'].queryset = Goal.objects.filter(user=user)

        # If editing, restrict fields based on goal
        goal = self.initial.get('goal') or self.data.get('goal')
        if goal:
            try:
                if isinstance(goal, Goal):
                    goal_obj = goal
                else:
                    goal_obj = Goal.objects.get(id=goal)
                allowed_metrics = goal_obj.get_metrics().keys()
                for field in ['tempo', 'mistakes', 'duration', 'accuracy']:
                    if field not in allowed_metrics:
                        self.fields.pop(field, None)
            except:
                pass
