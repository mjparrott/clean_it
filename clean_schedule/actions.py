from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from clean_schedule import forms
from clean_schedule.models import Group, CleanUser, TaskType

from datetime import datetime

def log_out(request):
  logout(request)
  return HttpResponseRedirect('/')

def create_schedule(request):
  # Created a schedule for this user's group
  # Get this users group
  group = request.user.cleanuser.group
  # Get all of the users in this group
  users = User.objects.filter(group=group)
  # need to find all of the task types for a group
  task_types = TaskType.objects.filter(group=group)
  # Create the schedule for the upcoming month
  
  total_tasks = 0
  current_user = 0
  today = datetime.today()
  tasks = []
  
  for task_type in task_types:
    # daily
    if task_type.freq == 1:
      for i in range(1, 29):
        i_days = timedelta(days = i)
        scheduled_date = today + i_days
        t = Task(user=users[current_user], datetime=scheduled_date)
        current_user += 1
        if current_user >= len(users):
          current_user = 0
        tasks.append(t)
    # weekly
    elif task_type.freq == 2:
      for i in range(0, 4):
        i_days = timedelta(weeks = i)
        scheduled_date = today + i_weeks
        t = Task(user=users[current_user], datetime=scheduled_date)
        current_user += 1
        if current_user >= len(users):
          current_user = 0
        tasks.append(t)
      total_tasks += 4
    # monthly
    elif task_type.freq == 3:
      scheduled_date = today + timedelta(weeks = 2)
      t = Task(user=users[current_user], datetime=scheduled_date)
      tasks.append(t)
      total_tasks += 1
  
  for task in tasks:
    task.save()

  return HttpResponseRedirect('/')
