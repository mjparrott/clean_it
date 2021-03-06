from django.conf.urls import patterns, url

from clean_schedule import actions, views

urlpatterns = patterns('',
  url(r'^groups/create_group', views.create_group, name='create_group'),
  url(r'^groups/add_group', views.add_to_group, name='add_to_group'),
  url(r'^groups/view_group', views.view_group, name='view_group'),
  url(r'^sign_up', views.sign_up, name='sign_up'),
  url(r'^log_in', views.log_in, name='log_in'),
  url(r'^log_out', actions.log_out, name='log_out'),
  url(r'^view_sched', views.view_sched, name='view_sched'),
  url(r'^create_schedule', actions.create_schedule, name='create_schedule'),
  url(r'^tasks/add_task', views.add_task, name='add_task'),
  url(r'^$', views.index, name='index'),
)

