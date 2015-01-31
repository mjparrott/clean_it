from django.conf.urls import patterns, url

from clean_schedule import views

urlpatterns = patterns('',
  url(r'^groups/create_group', views.create_group, name='create_group'),
  url(r'^sign_up', views.sign_up, name='sign_up'),
  url(r'^log_in', views.log_in, name='log_in'),
  url(r'^$', views.index, name='index'),
)

