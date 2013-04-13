from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from registration import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PolTrac.views.home', name='home'),
    # url(r'^PolTrac/', include('PolTrac.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'registration.views.home', name='home' ),
    url(r'^registration/', include('registration.urls')),
  
)
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()