from django.conf.urls import patterns, url

from clean_schedule import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
)
