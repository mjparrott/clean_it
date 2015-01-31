from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.utils import timezone

from clean_schedule import forms
from clean_schedule.models import Group, CleanUser, TaskType, Task

from datetime import datetime, timedelta

# Create your views here.
def index(request):
  template = loader.get_template('clean_schedule/index.html')
  context = RequestContext(request, {})
  return HttpResponse(template.render(context),
  {
    'user': request.user
  })

def sign_up(request):
  # If this is a POST request we need to process the form data
  if request.method == 'POST':
    # Create a form instance and populate it with data from the request:
    form = forms.SignUpForm(request.POST)
    # Check whether it's valid:
    if form.is_valid():
      # processs data here...
      # create the user
      user = User.objects.create_user(form.cleaned_data['user_name'], form.cleaned_data['email'],
        form.cleaned_data['password'])
      user.save()
      clean_user = CleanUser(user = user, group = Group())
      clean_user.save()
      # redirect
      return HttpResponseRedirect('/')
  else:
    # create a blank form
    form = forms.SignUpForm()

  return render(request, 'clean_schedule/sign_up.html', {'form': form})

def log_in(request):
  # If this is a POST request we need to process the form data
  if request.method == 'POST':
    # Create a form instance and populate it with data from the request:
    form = forms.LoginForm(request.POST)
    # Check whether it's valid:
    if form.is_valid():
      # processs data here...
      # log in the user
      username = form.cleaned_data['user_name']
      password = form.cleaned_data['password']
      user = authenticate(username=username, password=password)
      if user is not None:
        if user.is_active:
          login(request, user)
          return HttpResponseRedirect('/')
  else:
    # create a blank form
    form = forms.LoginForm()

  return render(request, 'clean_schedule/log_in.html', {'form': form})

def create_group(request):
  if request.method == 'POST':
    form = forms.CreateGroupForm(request.POST)
    if form.is_valid():
      group_name = form.cleaned_data['group_name']
      g = Group(name=group_name)
      # also add user to the group as admin
      g.save()
      # update the user
      user = request.user.cleanuser
      
      user.group = g
      user.save()
      return HttpResponseRedirect('/')
  else:
    form = forms.CreateGroupForm()
  
  return render(request, 'clean_schedule/groups/create_group.html', {'form': form})

def add_to_group(request):
  if request.method == 'POST':
    form = forms.AddToGroupForm(request.POST)
    if form.is_valid():
      member_name = form.cleaned_data['member_name']
      user = User.objects.get(username=member_name)
      clean_user = user.cleanuser
      clean_user.group = request.user.cleanuser.group
      clean_user.save()
      return HttpResponseRedirect('/')
  else:
    form = forms.AddToGroupForm()

  return render(request, 'clean_schedule/groups/add_group.html', {'form': form})

def add_task(request):
  if request.method == 'POST':
    form = forms.AddTaskForm(request.POST)
    if form.is_valid():
      task_name = form.cleaned_data['task_name']
      weight = form.cleaned_data['weight']
      freq = form.cleaned_data['freq']
      group = request.user.cleanuser.group
      t = TaskType(type=task_name, weight=weight, freq=freq, group=group)
      t.save()
      return HttpResponseRedirect('/')
  else:
    form = forms.AddTaskForm()
    
  return render(request, 'clean_schedule/tasks/add_task.html', {'form': form})

def view_group(request):
  group = request.user.cleanuser.group
  users_in_group = CleanUser.objects.filter(group=group)
  users = map(lambda x: x.user, users_in_group)

  return render(request, 'clean_schedule/groups/view_group.html', {'users': users })

def view_sched(request):
  my_tasks = Task.objects.filter(user = request.user.cleanuser)
  my_tasks = sorted(list(my_tasks), key = lambda x: x.datetime)
  today = timezone.now() # datetime.today().replace(tzinfo=None)
  day_buckets = [[]] * 28

  
  for i in range(1, 29):
    for ind in range(len(my_tasks)):
      if my_tasks[ind].datetime - today < timedelta(days = i) and my_tasks[ind].datetime - today > timedelta(days = i - 1):
        day_buckets[i - 1].append(my_tasks[ind])
        #ind -= 1
  day_buckets = list(enumerate(day_buckets))
  for i in range(0, 28):
    day_buckets[i] = (day_buckets[i][0], i % 7 == 0, (i + 1) % 7 == 0, day_buckets[i][1])
  #error = reor

  return render(request, 'clean_schedule/view_sched.html', {'day_tasks': day_buckets, 'username': request.user.username})
