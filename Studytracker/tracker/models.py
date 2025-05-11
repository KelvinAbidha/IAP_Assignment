from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class StudyGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    target_hours = models.FloatField()
    deadline = models.DateField()
    reminder_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.title

class StudyLog(models.Model):
    goal = models.ForeignKey(StudyGoal, on_delete=models.CASCADE)
    date = models.DateField()
    hours_spent = models.FloatField()

    def __str__(self):
        return f"{self.goal.title} - {self.hours_spent} hrs on {self.date}"

