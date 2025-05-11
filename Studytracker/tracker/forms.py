from django import forms
from .models import StudyGoal, StudyLog

class StudyGoalForm(forms.ModelForm):
    class Meta:
        model = StudyGoal
        fields = ['title', 'description', 'target_hours', 'deadline', 'reminder_time']

class StudyLogForm(forms.ModelForm):
    class Meta:
        model = StudyLog
        fields = ['goal', 'date', 'hours_spent']
