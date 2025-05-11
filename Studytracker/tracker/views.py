
from django.shortcuts import render, redirect
from .models import StudyGoal, StudyLog
from .forms import StudyGoalForm, StudyLogForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.mail import send_mail
from django.utils import timezone
import datetime

from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def dashboard(request):
    goals = StudyGoal.objects.filter(user=request.user)
    logs = StudyLog.objects.filter(goal__user=request.user)

    # Send email reminders if current time is near reminder_time
    now = timezone.localtime().time()
    for goal in goals:
        if goal.reminder_time and abs((datetime.datetime.combine(datetime.date.today(), goal.reminder_time) - datetime.datetime.combine(datetime.date.today(), now)).seconds) < 300:
            send_mail(
                'Study Reminder',
                f"Don't forget to study for: {goal.title}",
                'your_email@gmail.com',  # Change this to your sending address
                [request.user.email],
                fail_silently=True,
            )

    return render(request, 'tracker/dashboard.html', {'goals': goals, 'logs': logs})

@login_required
def add_goal(request):
    if request.method == 'POST':
        form = StudyGoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect('dashboard')
    else:
        form = StudyGoalForm()
    return render(request, 'tracker/add_goal.html', {'form': form})

@login_required
def add_log(request):
    if request.method == 'POST':
        form = StudyLogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = StudyLogForm()
    return render(request, 'tracker/add_log.html', {'form': form})

@login_required
def chart_data(request):
    logs = StudyLog.objects.filter(goal__user=request.user)
    data = {}
    for log in logs:
        if log.goal.title not in data:
            data[log.goal.title] = 0
        data[log.goal.title] += log.hours_spent
    return JsonResponse(data)

