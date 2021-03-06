from django.conf.urls.defaults import *

from views import *
from races.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    # Site Root
    #(r'^$', homepage),
    #(r'^time/plus/(\d{1,2})/$', hours_ahead),
    #(r'^current_time/$', current_datetime),
    #(r'^hello/', hello),
)

# race URLs
urlpatterns += patterns('',
    url(r'^races/', include('races.urls')),
)
