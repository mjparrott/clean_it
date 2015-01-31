from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from clean_schedule import forms
from clean_schedule.models import Group, CleanUser

def log_out(request):
  logout(request)
  return HttpResponseRedirect('/')
