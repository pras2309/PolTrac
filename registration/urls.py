from django.conf.urls import patterns, url

from registration import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^index/$', views.register, name='register'),
    url(r'^list/$', views.list, name='list'),
    url(r'^profile/(?P<id>\d)/$', views.profile, name='profile')
)