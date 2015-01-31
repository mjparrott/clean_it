from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from clean_schedule import forms
from clean_schedule.models import Group, CleanUser

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

  return render(request, '/sign_up.html', {'form': form})

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

  return render(request, '/log_in.html', {'form': form})

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
  
  return render(request, '/create_group.html', {'form': form})
