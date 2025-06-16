from django import forms
from .models import Goal, PracticeSession


class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['title', 'description', 'standard_goal', 'target_date']
        widgets = {
            'target_date': forms.DateInput(attrs={'type': 'date'}),
        }

    # Custom goal metric fields
    starting_tempo = forms.IntegerField(required=False, label="Starting Tempo")
    target_tempo = forms.IntegerField(required=False, label="Target Tempo")
    duration = forms.IntegerField(required=False, label="Target Duration (minutes)")
    mistakes = forms.IntegerField(required=False, label="Max Mistakes per Repetition")

    def clean(self):
        cleaned_data = super().clean()

        if not cleaned_data.get('standard_goal'):
            metrics = {}

            # Handle tempo range
            start = cleaned_data.get('starting_tempo')
            target = cleaned_data.get('target_tempo')
            if start is not None or target is not None:
                metrics['tempo'] = {
                    'start': start or 0,
                    'target': target or 0
                }

            # Other metrics
            if cleaned_data.get('duration') is not None:
                metrics['duration'] = cleaned_data['duration']
            if cleaned_data.get('mistakes') is not None:
                metrics['mistakes'] = cleaned_data['mistakes']

            cleaned_data['metrics'] = metrics

        return cleaned_data
    
    def clean_metrics(self):
        metrics = self.cleaned_data['metrics']
        if any(isinstance(v, dict) for v in metrics.values()):
            raise forms.ValidationError("Metric values must be flat numbers, not dictionaries.")
        return metrics

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
