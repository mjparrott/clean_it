from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from clean_schedule import forms

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
      # redirect
      return HttpResponseRedirect('/clean_schedule')
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
          return HttpResponseRedirect('/clean_schedule')
  else:
    # create a blank form
    form = forms.LoginForm()

  return render(request, 'clean_schedule/log_in.html', {'form': form})

