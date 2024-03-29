from django.conf.urls.defaults import *
from traffic.views import index, start_map

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
        ('^$', index),
        ('^traffic/in/(johannesburg||cape town||pretoria)$', start_map),
        # Example:
    # (r'^traffic/', include('traffic.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^admin/', include(admin.site.urls)),
)
