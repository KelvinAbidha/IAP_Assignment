from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add_goal/', views.add_goal, name='add_goal'),
    path('add_log/', views.add_log, name='add_log'),
    path('chart_data/', views.chart_data, name='chart_data'),
    path('register/', views.register, name='register'),
]
