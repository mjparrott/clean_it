from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
  # Examples:
  # url(r'^$', 'clean_it.views.home', name='home'),
  # url(r'^blog/', include('blog.urls')),
  
  url(r'^admin/', include(admin.site.urls)),
  url(r'^clean_schedule/', include('clean_schedule.urls')),
)
