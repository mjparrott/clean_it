from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render

from clean_schedule import forms

# Create your views here.
def index(request):
  template = loader.get_template('clean_schedule/index.html')
  context = RequestContext(request, {})
  return HttpResponse(template.render(context))

def sign_up(request):
  # If this is a POST request we need to process the form data
  if request.method == 'POST':
    # Create a form instance and populate it with data from the request:
    form = forms.SignUpForm(request.POST)
    # Check whether it's valid:
    if form.is_valid():
      # processs data here...
      # redirect
      return HttpResponseRedirect('/clean_schedule')
  else:
    # create a blank form
    form = forms.SignUpForm()

  return render(request, 'clean_schedule/sign_up.html', {'form': form})
