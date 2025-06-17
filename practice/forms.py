from django import forms
from .models import Goal, PracticeSession


class GoalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # Make all conditional fields non-required
        self.fields['target_tempo'].required = False
        self.fields['target_accuracy'].required = False
        self.fields['target_duration'].required = False
        self.fields['routine_target_days'].required = False

    class Meta:
        model = Goal
        fields = [
            'title', 'description', 'goal_type', 'standard_goal',
            'target_tempo', 'target_accuracy', 'target_duration',
            'routine_target_days', 'target_date'
        ]
        widgets = {
            'target_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        goal_type = cleaned_data.get('goal_type')

        # Routine goal check
        if goal_type == 'routine':
            if not cleaned_data.get('routine_target_days'):
                self.add_error('routine_target_days', 'This field is required for routine goals.')

            # Routine should NOT use tempo/accuracy/duration
            for field in ['target_tempo', 'target_accuracy', 'target_duration']:
                if cleaned_data.get(field):
                    self.add_error(field, f"{field.replace('_', ' ').capitalize()} is not allowed for routine goals.")

        # Technical or custom goal check
        elif goal_type in ['technique', 'custom']:
            required_fields = ['target_tempo', 'target_accuracy', 'target_duration']
            missing = [f for f in required_fields if not cleaned_data.get(f)]
            if missing:
                raise forms.ValidationError(
                    f"Fields required for {goal_type} goals: {', '.join(missing)}"
                )

        # Repertoire goals: no numeric attributes
        elif goal_type == 'repertoire':
            for field in ['target_tempo', 'target_accuracy', 'target_duration', 'routine_target_days']:
                if cleaned_data.get(field):
                    self.add_error(field, f"{field.replace('_', ' ').capitalize()} is not allowed for repertoire goals.")

        return cleaned_data


class PracticeSessionForm(forms.ModelForm):
    class Meta:
        model = PracticeSession
        fields = ['goal', 'date', 'duration', 'tempo', 'accuracy', 'notes']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['goal'].queryset = Goal.objects.filter(user=user)

        # Try to fetch the goal object from initial or form data
        goal_instance = None
        raw_goal = self.initial.get('goal') or self.data.get('goal')
        if raw_goal:
            try:
                goal_instance = raw_goal if isinstance(raw_goal, Goal) else Goal.objects.get(pk=raw_goal)
            except Goal.DoesNotExist:
                pass

        # Adjust fields based on goal type
        if goal_instance:
            if goal_instance.goal_type in ['repertoire', 'routine']:
                self.fields.pop('tempo', None)
                self.fields.pop('accuracy', None)
