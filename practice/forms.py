from django import forms
from .models import Goal, PracticeSession


class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['title', 'description']


class PracticeSessionForm(forms.ModelForm):
    class Meta:
        model = PracticeSession
        fields = '__all__'
