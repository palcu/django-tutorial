from django.conf.urls import patterns, include, url
from mysite.views import hello, current_datetime, hours_ahead, display_meta
from django.contrib import admin
from contact import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    ('^hello/$', hello),
    ('^time/$', current_datetime),
    ('^meta/$', display_meta),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    # (r'^search/$', views.search),
    (r'^contact/$', views.contact),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
