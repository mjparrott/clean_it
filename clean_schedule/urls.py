from django.conf.urls import patterns, url

from clean_schedule import views

urlpatterns = patterns('',
  url(r'^sign_up', views.sign_up, name='sign_up'),
  url(r'^$', views.index, name='index'),
)
